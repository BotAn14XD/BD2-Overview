document.addEventListener("DOMContentLoaded", function() {
    const times = document.querySelectorAll(".local-time");
    times.forEach(element => {
        const utcStr = element.getAttribute("data-utc");
        if (!utcStr) return;
        const [hours, minutes] = utcStr.split(':');
        const date = new Date();
        date.setUTCHours(parseInt(hours), parseInt(minutes), 0);
        const localTime = date.toLocaleTimeString([], { 
            hour: '2-digit', 
            minute: '2-digit'
        });
        element.textContent = localTime;
        element.title = `${utcStr} UTC (Your Local Time)`;
        element.style.cursor = "help";
        element.style.borderBottom = "1px dotted #888";
    });
});