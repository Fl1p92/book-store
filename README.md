# book-store
Simple book store with some features:
* in main page you can see list of books with following information: book title, authors info, ISBN, price, publish date. Also you can order list of books by publish date(asc/desc);
* separate page where we can create/edit book data;
* calendar widget(bootstrap-datepicker) to set pulish date on the edit page;
* link to admin edit page beside each of books on the main page;
* custom **SaveRequestMiddleware** and model for possibility to save all http requests to database. The separete page for display 10 last of then;
* site copyright with start/end years;
* custom signals and model for logging of books manipulations: create/edit/delete. The separete page for display 10 last of then.
