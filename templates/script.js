// script.js

// Function to issue a new book
function issueBook(event) {
    event.preventDefault(); // Prevent form submission

    // Get the form values
    const bookName = document.getElementById('bookName').value;
    const authorName = document.getElementById('authorName').value;
    const issueDate = document.getElementById('issueDate').value;
    const returnDate = document.getElementById('returnDate').value;

    // Create an object for the book data
    const book = {
        bookName,
        authorName,
        issueDate,
        returnDate
    };

    // Get existing issued books from localStorage
    const issuedBooks = JSON.parse(localStorage.getItem('issuedBooks')) || [];

    // Add the new book to the list of issued books
    issuedBooks.push(book);

    // Save the updated list back to localStorage
    localStorage.setItem('issuedBooks', JSON.stringify(issuedBooks));

    // Reset the form
    document.getElementById('issueForm').reset();

    // Update the displayed list of books
    displayIssuedBooks();
}

// Function to display issued books from localStorage
function displayIssuedBooks() {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = ''; // Clear the list

    // Get the issued books from localStorage
    const issuedBooks = JSON.parse(localStorage.getItem('issuedBooks')) || [];

    // Display each issued book as a list item
    issuedBooks.forEach((book, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <div>
                <strong>${book.bookName}</strong> by ${book.authorName} <br>
                Issued: ${book.issueDate} | Return: ${book.returnDate}
            </div>
            <button class="remove-btn" onclick="removeBook(${index})">Remove</button>
        `;
        bookList.appendChild(listItem);
    });
}

// Function to remove a book from the list
function removeBook(index) {
    // Get the issued books from localStorage
    const issuedBooks = JSON.parse(localStorage.getItem('issuedBooks')) || [];

    // Remove the selected book
    issuedBooks.splice(index, 1);

    // Save the updated list back to localStorage
    localStorage.setItem('issuedBooks', JSON.stringify(issuedBooks));

    // Update the displayed list of books
    displayIssuedBooks();
}

// Add event listener to the form
document.getElementById('issueForm').addEventListener('submit', issueBook);

// Display the issued books on page load
document.addEventListener('DOMContentLoaded', displayIssuedBooks);

