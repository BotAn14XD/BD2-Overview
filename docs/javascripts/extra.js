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