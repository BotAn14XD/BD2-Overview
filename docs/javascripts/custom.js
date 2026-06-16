function manageDiscordBanner() {
    if (localStorage.getItem("discordBannerClosed") !== "true") {
        let bannerWrapper = document.querySelector(".md-banner");
        let innerBar = document.getElementById("discord-announce-bar");
        
        if (bannerWrapper) bannerWrapper.style.display = "block";
        if (innerBar) innerBar.style.display = "flex";
    }
}

if (typeof document$ !== "undefined") {
    document$.subscribe(manageDiscordBanner);
} else {
    document.addEventListener("DOMContentLoaded", manageDiscordBanner);
}

function closeAnnounceBar() {
    let bannerWrapper = document.querySelector(".md-banner");

    if (bannerWrapper) {
        bannerWrapper.style.display = "none";
    }
    localStorage.setItem("discordBannerClosed", "true");
}

document.addEventListener("DOMContentLoaded", function () {
    const timeElements = document.querySelectorAll('.local-time');

    timeElements.forEach(element => {
        const utcTimeString = element.getAttribute('data-utc');
        
        try {
            const utcDate = new Date(utcTimeString.includes('Z') ? utcTimeString : utcTimeString + ' UTC');
            const localTimeString = utcDate.toLocaleString(undefined, {
                dateStyle: 'medium',
                timeStyle: 'short'
            });
            element.textContent = localTimeString;
        } catch (error) {
            console.error("Failed to parse UTC time for element:", element, error);
        }
    });
});