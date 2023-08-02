Sure, I'll create a simple database schema for the Crypto Trading simulation app based on your requirements. Please modify as necessary for your specific implementation.

Database Schema:

1. **Users Table**

| Field      | Type        | Description             |
| ----------- | ----------- | ----------------------- |
| id        | Integer     | Primary Key             |
| username  | String      | Unique username         |
| email     | String      | Unique email address    |
| password  | String      | Hashed password         |
| balance   | Decimal     | Game money balance      |

2. **Coins Table**

| Field      | Type        | Description             |
| ----------- | ----------- | ----------------------- |
| id        | Integer     | Primary Key             |
| name      | String      | Coin name               |
| symbol    | String      | Coin symbol             |
| price     | Decimal     | Current price of coin   |

3. **Portfolio Table**

| Field     | Type        | Description                   |
| ----------| ----------- | ----------------------------- |
| id        | Integer     | Primary Key                   |
| user_id   | Integer     | Foreign Key referencing Users |
| coin_id   | Integer     | Foreign Key referencing Coins |
| quantity  | Decimal     | Quantity of coin held         |

4. **Transactions Table**

| Field     | Type        | Description                   |
| ----------| ----------- | ----------------------------- |
| id        | Integer     | Primary Key                   |
| user_id   | Integer     | Foreign Key referencing Users |
| coin_id   | Integer     | Foreign Key referencing Coins |
| quantity  | Decimal     | Quantity of coin bought/sold  |
| price     | Decimal     | Price at which transacted     |
| type      | String      | Type of transaction (buy/sell)|
| timestamp | DateTime    | Time of transaction           |

5. **Coin History Table**

| Field     | Type        | Description                   |
| ----------| ----------- | ----------------------------- |
| id        | Integer     | Primary Key                   |
| coin_id   | Integer     | Foreign Key referencing Coins |
| price     | Decimal     | Price of coin                 |
| timestamp | DateTime    | Time of price record          |

These are the main tables you'll need to support the functionality you described. You might also need additional tables or fields depending on your exact requirements. Remember to use appropriate indexing, constraints, and relations to ensure data integrity and performance. Also consider using views or stored procedures for complex queries or operations.

Remember to replace "Decimal" with the appropriate numeric data type for your specific SQL variant. Some databases use "Decimal", while others might use "Float" or "Numeric".