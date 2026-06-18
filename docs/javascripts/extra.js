document.addEventListener("DOMContentLoaded", function() {
    const times = document.querySelectorAll(".local-time");
    
    times.forEach(element => {
        const utcStr = element.getAttribute("data-utc");
        if (!utcStr) return;
        
        const matches = utcStr.match(/^(\d{1,2}):(\d{2})$/);
        if (!matches) return;
        
        const hours = parseInt(matches[1], 10);
        const minutes = parseInt(matches[2], 10);
        
        const dummyDate = new Date(Date.UTC(2026, 0, 1, hours, minutes, 0)); 
        
        const localTime = dummyDate.toLocaleTimeString([], { 
            hour: '2-digit', 
            minute: '2-digit'
        });
        
        element.textContent = localTime;
        element.title = `${utcStr} UTC is ${localTime} in your local time`;
        
        element.style.cursor = "help";
        element.style.borderBottom = "1px dotted #888";
        element.style.display = "inline-block"; 
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const wrappers = document.querySelectorAll(".gear-tooltip-wrapper");

    function adjustTooltipPosition(wrapper) {
        const tooltip = wrapper.querySelector(".gear-tooltip-box");
        if (!tooltip) return;

        tooltip.style.left = "50%";
        tooltip.style.transform = "translateX(-50%)";

        requestAnimationFrame(() => {
            const rect = wrapper.getBoundingClientRect();
            const tooltipRect = tooltip.getBoundingClientRect();
            const viewportWidth = window.innerWidth;

            if (rect.top < 250) {
                tooltip.style.bottom = "auto";
                tooltip.style.top = "125%";
                tooltip.classList.add("flipped-down");
            } else {
                tooltip.style.bottom = "125%";
                tooltip.style.top = "auto";
                tooltip.classList.remove("flipped-down");
            }
            const padding = 12; 
            let shiftX = 0;

            if (tooltipRect.left < padding) {
                shiftX = padding - tooltipRect.left;
            } else if (tooltipRect.right > viewportWidth - padding) {
                shiftX = (viewportWidth - padding) - tooltipRect.right;
            }

            // Apply shifts safely using translate
            if (shiftX !== 0) {
                tooltip.style.transform = `translateX(calc(-50% + ${shiftX}px))`;
            }
        });
    }

    wrappers.forEach(wrapper => {
        wrapper.addEventListener("mouseenter", () => adjustTooltipPosition(wrapper));
        
        // Mobile tap support
        wrapper.addEventListener("touchstart", function(e) {
            adjustTooltipPosition(this);
        }, { passive: true });
    });
});