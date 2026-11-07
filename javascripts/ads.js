function checkAdBlocker() {
    setTimeout(function () {
        const adElement = document.querySelector(".md-ad--content-bottom ins.adsbygoogle");
        const fallback = document.getElementById("support-fallback");
        const adContainer = document.querySelector(".md-ad--content-bottom");

        if (!fallback) return;

        // An ad blocker is active if:
        // 1. adsbygoogle is not loaded/pushed properly
        // 2. The element was collapsed to 0 height or set to display: none
        const isBlocked = !adElement || 
                          adElement.offsetHeight === 0 || 
                          adElement.style.display === "none" ||
                          adElement.getAttribute("data-ad-status") === "unfilled";

        if (isBlocked) {
            if (adContainer) adContainer.style.display = "none";
            fallback.style.display = "block";
        }
    }, 600); // Small delay to give AdSense time to mount
}

function pushAd() {
    try {
        (window.adsbygoogle = window.adsbygoogle || []).push({});
    } catch (e) {
        /* Script blocked */
    }
    checkAdBlocker();
}

document.addEventListener("DOMContentLoaded", function () {
    pushAd();
    if (typeof document$ !== "undefined") {
        document$.subscribe(pushAd);
    }
});