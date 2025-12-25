document.addEventListener('DOMContentLoaded', () => {
    const needle = document.getElementById('needle');
    const cpsDisplay = document.getElementById('cps-display');
    const clickButton = document.getElementById('click-button');

    let clickTimestamps = [];
    const REQUIRED_CPS = 8;
    const MAX_CPS_DISPLAY = 8;
    const WINDOW_MS = 1000;

    clickButton.addEventListener('mousedown', () => {
        clickTimestamps.push(performance.now());
    });

    setInterval(() => {
        const now = performance.now();
        
        clickTimestamps = clickTimestamps.filter(ts => now - ts < WINDOW_MS);
        
        const currentCPS = clickTimestamps.length;
        
        const angle = Math.min((currentCPS / MAX_CPS_DISPLAY), 1) * 180 - 90;
        needle.style.transform = `translateX(-50%) rotate(${angle}deg)`;
        
        cpsDisplay.textContent = `CPS: ${currentCPS}`;

        if (currentCPS >= REQUIRED_CPS) {
            clickTimestamps = [];
            window.location.href = '/succex'; 
        }
    }, 33);
});