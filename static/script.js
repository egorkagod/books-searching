// Загрузка книг в виде JSON

const batchLoadBooks = () => {
    let data;

    try {
        data = JSON.parse(document.getElementById("json").value)
    } catch (e) {
        showInfo("batch-load-info", "Ошибка формата JSON", true);
        console.error(e);
        return;
    }
    if (!Array.isArray(data)) {
        showInfo("batch-load-info", "Нужно передать JSON-массив [{...}, {...}]", true);
        return;
    }
    fetch("/books/batch-load", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        showInfo("batch-load-info", data.message ?? "Ошибка при загрузки книг", false);
    })
    .catch(err => console.error(err))
}

document.getElementById("batch-load-form").addEventListener("submit", function(e) {
    e.preventDefault();
    batchLoadBooks();
});

// Загрузка книги

const getNewBook = () => { 
    return {
        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        year: Number(document.getElementById("year").value),
        category: document.getElementById("category").value,
        description: document.getElementById("description").value
    }
};

const loadBook = () => {
    fetch("/books/load", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(getNewBook())
    })
    .then(res => res.json())
    .then(data => {
        showInfo("load-info", data.message, false);
    })
    .catch(err => console.error(err));
};

document.getElementById("load-form").addEventListener("submit", function(e) {
    e.preventDefault();
    loadBook();
});

// Поиск книг

const getBookCard = (book) => {
    return `
        <div class="card">
            <h3>${book.entity.title} ${book.entity.year}</h3>
            <p>${book.entity.description}</p>
            <h4>Автор: ${book.entity.author}</h4>
        </div>
    `
};

const getSearchParams = (query) => {
    return new URLSearchParams({
        query: query,
        limit: 5
    })
};

const showBooks = (books) => {
    const container = document.getElementById("books");
    container.innerHTML = books.map(getBookCard).join("");
};

const searchBooks = () => {
    const queryString = document.getElementById("query").value.trim();
    if (queryString.length < 3) {
        showInfo("search-info", "Введите хотя бы 3 символа для поиска", true);
        return;
    }

    fetch(`/books/search?${getSearchParams(queryString).toString()}`, {
        method: "GET",
    })
    .then(res => res.json())
    .then(books => {
        showInfo("search-info", books.message, false);
        showBooks(books.books ?? []);
    })
    .catch(err => console.error(err));
};

document.getElementById("search-form").addEventListener("submit", function(e) {
    e.preventDefault();
    searchBooks();
});

// Общие функции

const showInfo = (id, text, isError) => {
    const container = document.getElementById(id);
    if (isError) {
        container.style.color = "red";
    } else {
        container.style.color = "green";
    }
    container.innerText = text;
    container.style.display = "block";
}