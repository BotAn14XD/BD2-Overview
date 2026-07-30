function manageSurveyBanner() {
    if (localStorage.getItem("surveyBannerClosed") !== "true") {
        let bannerWrapper = document.querySelector(".md-banner");
        let innerBar = document.getElementById("survey-announce-bar");

        if (bannerWrapper) bannerWrapper.style.display = "block";
        if (innerBar) innerBar.style.display = "flex";
    }
}

if (typeof document$ !== "undefined") {
    document$.subscribe(manageSurveyBanner);
} else {
    document.addEventListener("DOMContentLoaded", manageSurveyBanner);
}

function closeSurveyBar() {
    let bannerWrapper = document.querySelector(".md-banner");

    if (bannerWrapper) {
        bannerWrapper.style.display = "none";
    }
    localStorage.setItem("surveyBannerClosed", "true");
}

document.addEventListener("DOMContentLoaded", function() {
    const times = document.querySelectorAll(".local-time");

    times.forEach(element => {
        const utcStr = element.getAttribute("data-utc");
        if (!utcStr) return;

        const matches = utcStr.match(/^(\d{1,2}):(\d{2})$/);
        if (!matches) return;

        const hours = parseInt(matches[1], 10);
        const minutes = parseInt(matches[2], 10);

        const now = new Date();
        const dummyDate = new Date(Date.UTC(
            now.getUTCFullYear(), 
            now.getUTCMonth(), 
            now.getUTCDate(), 
            hours, 
            minutes, 
            0
        ));

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

function initTooltips() {
    const wrappers = document.querySelectorAll(".gear-tooltip-wrapper");

    function adjustTooltipPosition(wrapper) {
        const tooltip = wrapper.querySelector(".gear-tooltip-box");
        if (!tooltip) return;

        tooltip.style.display = "block";
        tooltip.style.left = "50%";
        tooltip.style.transform = "translateX(-50%)";

        const rect = wrapper.getBoundingClientRect();
        const tooltipRect = tooltip.getBoundingClientRect();

        const mainContent = document.querySelector(".md-content") || document.querySelector("article");

        let minLeftBoundary = 16;
        let maxRightBoundary = window.innerWidth - 16;

        if (mainContent) {
            const contentRect = mainContent.getBoundingClientRect();
            minLeftBoundary = contentRect.left + 16;
            maxRightBoundary = Math.min(window.innerWidth - 16, contentRect.right - 16);
        }

        if (rect.top < 250) {
            tooltip.style.bottom = "auto";
            tooltip.style.top = "125%";
            tooltip.classList.add("flipped-down");
        } else {
            tooltip.style.bottom = "125%";
            tooltip.style.top = "auto";
            tooltip.classList.remove("flipped-down");
        }

        let shiftX = 0;

        if (tooltipRect.left < minLeftBoundary) {
            shiftX = minLeftBoundary - tooltipRect.left;
        } else if (tooltipRect.right > maxRightBoundary) {
            shiftX = maxRightBoundary - tooltipRect.right;
        }

        if (shiftX !== 0) {
            tooltip.style.transform = `translateX(calc(-50% + ${shiftX}px))`;
        }

        tooltip.style.display = "";
    }

    wrappers.forEach(wrapper => {
        if (wrapper.dataset.tooltipInit) return;
        wrapper.dataset.tooltipInit = "true";

        wrapper.addEventListener("mouseenter", () => adjustTooltipPosition(wrapper));
        wrapper.addEventListener("touchstart", function() {
            adjustTooltipPosition(this);
        }, { passive: true });
    });
}

if (typeof document$ !== "undefined") {
    document$.subscribe(function() {
        initTooltips();
    });
} else {
    document.addEventListener("DOMContentLoaded", initTooltips);
}

document.addEventListener('click', function (event) {
    const button = event.target.closest('.share-btn');
    if (!button) return;

    event.stopPropagation();

    const anchorId = button.getAttribute('data-anchor');
    const shareUrl = `${window.location.origin}${window.location.pathname}#${anchorId}`;

    navigator.clipboard.writeText(shareUrl).then(() => {
        button.value = 'Copied!';
        button.classList.add('copied');
        setTimeout(() => {
            button.value = 'Copy Share Link';
            button.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
});