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

    wrappers.forEach(wrapper => {
        wrapper.addEventListener("mouseenter", function() {
            const tooltip = this.querySelector(".gear-tooltip-box");
            if (!tooltip) return;

            const rect = this.getBoundingClientRect();
            
            if (rect.top < 250) {
                tooltip.style.bottom = "auto";
                tooltip.style.top = "125%";
                
                tooltip.classList.add("flipped-down");
            } else {
                tooltip.style.bottom = "125%";
                tooltip.style.top = "auto";
                tooltip.classList.remove("flipped-down");
            }
        });
    });
});