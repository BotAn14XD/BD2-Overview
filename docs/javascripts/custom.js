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