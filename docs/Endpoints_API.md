Here is a proposed list of API endpoints your application might expose, along with the HTTP methods, the data they will accept, and the data they will return. Note that the exact details will depend on your application's specifics, but this can serve as a good starting point:

1. **User Endpoints**

- `POST /api/register`
    - Accepts: username, email, password
    - Returns: success message, user data

- `POST /api/login`
    - Accepts: email, password
    - Returns: success message, user data, authentication token

- `GET /api/user/<id>`
    - Accepts: user id (in the URL)
    - Returns: user data

- `PUT /api/user/<id>`
    - Accepts: user id (in the URL), field(s) to be updated
    - Returns: success message, updated user data

2. **Coin Endpoints**

- `GET /api/coins`
    - Accepts: none
    - Returns: list of coins with current prices

- `GET /api/coin/<id>`
    - Accepts: coin id (in the URL)
    - Returns: coin data, including price history

3. **Portfolio Endpoints**

- `GET /api/portfolio/<user_id>`
    - Accepts: user id (in the URL)
    - Returns: list of coins user owns, with quantities

- `POST /api/portfolio/<user_id>/buy`
    - Accepts: user id (in the URL), coin id, quantity
    - Returns: success message, updated user balance, updated portfolio data

- `POST /api/portfolio/<user_id>/sell`
    - Accepts: user id (in the URL), coin id, quantity
    - Returns: success message, updated user balance, updated portfolio data

4. **Transaction Endpoints**

- `GET /api/transactions/<user_id>`
    - Accepts: user id (in the URL)
    - Returns: list of transactions made by the user

All the above endpoints should also return appropriate error messages for any kind of failed requests. Also, secure endpoints would typically require an Authorization header with a valid token.

In a real application, you should also consider pagination, especially for potentially large lists (like transactions or coins). For instance, the `GET /api/coins` endpoint could accept optional parameters for the page number and number of results per page.