const root = document.documentElement;

// ------------------------------------------
// THEME TOGGLE

const themeToggle = document.querySelector("#theme-toggle");

const moonIcon = `
    <svg class="theme-icon" viewBox="0 0 24 24"
         fill="none" stroke="currentColor" stroke-width="1.8"
         stroke-linecap="round" stroke-linejoin="round"
         aria-hidden="true">
        <path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5
                 8.5 8.5 0 1 0 20.5 14.5Z"/>
    </svg>
`;

const sunIcon = `
    <svg class="theme-icon" viewBox="0 0 24 24"
         fill="none" stroke="currentColor" stroke-width="1.8"
         stroke-linecap="round" stroke-linejoin="round"
         aria-hidden="true">
        <circle cx="12" cy="12" r="4"/>
        <path d="M12 2v2"/>
        <path d="M12 20v2"/>
        <path d="m4.93 4.93 1.42 1.42"/>
        <path d="m17.65 17.65 1.42 1.42"/>
        <path d="M2 12h2"/>
        <path d="M20 12h2"/>
        <path d="m4.93 19.07 1.42-1.42"/>
        <path d="m17.65 6.35 1.42-1.42"/>
    </svg>
`;

function applyTheme(theme) {
    root.dataset.theme = theme;

    if (themeToggle) {
        const darkMode = theme === "dark";

        // Show the icon for the theme the user can switch to.
        themeToggle.innerHTML = darkMode ? sunIcon : moonIcon;

        themeToggle.setAttribute(
            "aria-label",
            darkMode ? "Switch to light theme" : "Switch to dark theme"
        );

        themeToggle.setAttribute("title", 
            darkMode ? "Switch to light mode" : "Switch to dark mode"
        );

        themeToggle.setAttribute("aria-pressed", String(darkMode));
    }
}

const savedTheme = localStorage.getItem("wordworld-theme");
applyTheme(savedTheme || "light");

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const nextTheme =
            root.dataset.theme === "dark" ? "light" : "dark";

        localStorage.setItem("wordworld-theme", nextTheme);
        applyTheme(nextTheme);
    });
}

// ------------------------------------------

// CATEGORY NAVIGATION
// ------------------------------------------

document.querySelectorAll(".category-card[data-url]").forEach(card => {
    card.addEventListener("click", () => {
        window.location.href = card.dataset.url;
    });
});

// ------------------------------------------
// SEARCH
// ------------------------------------------

const searchForm = document.querySelector("#search-form");
const searchInput = document.querySelector("#search-input");
const suggestions = document.querySelector("#search-suggestions");
const searchStatus = document.querySelector("#search-status");
const searchResults = document.querySelector("#search-results");

let searchTimeout;

async function requestSearch(query) {
    const response = await fetch(
        `/api/search/?q=${encodeURIComponent(query)}`
    );

    if (!response.ok) {
        throw new Error("Search request failed");
    }

    return response.json();
}

function clearSuggestions() {
    if (suggestions) {
        suggestions.replaceChildren();
        suggestions.hidden = true;
    }
}

function createSuggestion(subject) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "suggestion-item";
    button.setAttribute("role", "option");

    const name = document.createElement("span");
    name.className = "suggestion-name";
    name.textContent = subject.name;

    const description = document.createElement("span");
    description.className = "suggestion-description";
    description.textContent =
        `${subject.category} — ${subject.summary}`;

    button.append(name, description);

    button.addEventListener("click", () => {
        window.location.href = `/subject/${subject.slug}`;
    });

    return button;
}

function showSuggestions(results) {
    clearSuggestions();

    if (!suggestions || results.length === 0) {
        return;
    }

    results.forEach(subject => {
        suggestions.appendChild(createSuggestion(subject));
    });

    suggestions.hidden = false;
}

function showSearchResults(results, query) {
    if (!searchResults) {
        return;
    }

    searchResults.replaceChildren();
    searchResults.hidden = false;

    const heading = document.createElement("h2");
    heading.textContent = `Search results for "${query}"`;
    searchResults.appendChild(heading);

    if (results.length === 0) {
        const empty = document.createElement("p");
        empty.textContent = "No matching subjects found. Try another search.";
        searchResults.appendChild(empty);
        return;
    }

    results.forEach(subject => {
        const article = document.createElement("article");
        article.className = "subject-result";

        const category = document.createElement("p");
        category.className = "subject-category";
        category.textContent = subject.category;

        const title = document.createElement("h3");
        const link = document.createElement("a");
        link.href = `/subject/${subject.slug}`;
        link.textContent = subject.name;
        title.appendChild(link);

        const description = document.createElement("p");
        description.textContent = subject.summary;

        article.append(category, title, description);
        searchResults.appendChild(article);
    });
}

if (searchInput && suggestions) {
    searchInput.addEventListener("input", () => {
        clearTimeout(searchTimeout);

        const query = searchInput.value.trim();

        if (searchResults) {
            searchResults.hidden = true;
        }

        if (query.length < 2) {
            clearSuggestions();

            if (searchStatus) {
                searchStatus.textContent =
                    "Try a subject such as Mars, DNA, or the African elephant.";
            }

            return;
        }

        searchTimeout = setTimeout(async () => {
            try {
                const data = await requestSearch(query);
                showSuggestions(data.results);

                if (searchStatus) {
                    searchStatus.textContent =
                        data.count > 0
                            ? `${data.count} matching subject(s) found.`
                            : "No matching subjects found yet.";
                }
            } catch (error) {
                clearSuggestions();

                if (searchStatus) {
                    searchStatus.textContent =
                        "Search is temporarily unavailable.";
                }
            }
        }, 250);
    });
}

if (searchForm && searchInput) {
    searchForm.addEventListener("submit", async event => {
        event.preventDefault();

        const query = searchInput.value.trim();

        if (query.length < 2) {
            if (searchStatus) {
                searchStatus.textContent =
                    "Please enter at least two characters.";
            }
            return;
        }

        clearSuggestions();

        if (searchStatus) {
            searchStatus.textContent = "Searching...";
        }

        try {
            const data = await requestSearch(query);

            showSearchResults(data.results, query);

            if (searchStatus) {
                searchStatus.textContent =
                    `${data.count} matching subject(s) found.`;
            }

            searchResults?.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        } catch (error) {
            if (searchStatus) {
                searchStatus.textContent =
                    "Something went wrong. Please try again.";
            }
        }
    });
}

// Close suggestions when clicking outside the search form.
document.addEventListener("click", event => {
    if (searchForm && !searchForm.contains(event.target)) {
        clearSuggestions();
    }
});
