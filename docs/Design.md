# Requirements Document

## Project Title: Cryptocurrency Trading Simulation App

## Project Overview:
The project is to build a cryptocurrency trading simulation application that allows users to learn about cryptocurrency trading without investing real money. The app provides a virtual trading environment with simulated coin prices that fluctuates randomly. The application is initially targeting less than 10 users, each given a game money balance of £200 to begin trading. 

## 1. Target Users
The target users are people who are interested in learning about cryptocurrency trading without investing real money, gamers, and potential employers.

## 2. Functional Requirements

### 2.1. User Management

#### 2.1.1. Registration
Users should be able to register with a unique username, email, and password.

#### 2.1.2. Login
Users should be able to login using their registered email and password.

#### 2.1.3. Profile
Users should be able to view their profile, which includes their current balance and transaction history.

### 2.2. Coin Management

#### 2.2.1. Coin Data Generation
The app should generate a list of fake coins with random names and symbols.

#### 2.2.2. Coin Price Simulation
The app should simulate coin prices, which change randomly every 5 minutes.

#### 2.2.3. Coin Price History
The app should keep a history of the simulated coin prices, which users can view.

### 2.3. Portfolio Management

#### 2.3.1. Portfolio Viewing
Users should be able to view their portfolio, which includes the coins they own and their current value.

#### 2.3.2. Coin Buying
Users should be able to buy coins, which deducts from their balance and adds to their portfolio.

#### 2.3.3. Coin Selling
Users should be able to sell coins from their portfolio, which adds to their balance.

### 2.4. Transactions

#### 2.4.1. Transaction Recording
The app should record every transaction made by a user, whether buying or selling coins.

#### 2.4.2. Transaction History Viewing
Users should be able to view their transaction history.

## 3. Non-functional Requirements

### 3.1. Performance
The app should have fast response times and be able to handle multiple concurrent users efficiently.

### 3.2. Scalability
The app should be designed to scale horizontally to handle increased user traffic.

### 3.3. Security
The app should have secure user authentication, using hashed passwords and token-based authentication. API endpoints should be protected from unauthorized access.

### 3.4. Maintainability
The code should be modular, well-documented, and easy to understand to ensure easy maintenance and updates.

### 3.5. Compatibility
The app should be compatible with major web browsers and devices.

### 3.6. Technology Stack
The app should be built using Flask for the backend API, PostgreSQL for the database, and React for the frontend.

## 4. Integrations
No third-party integrations are required as the coin data and prices are simulated and not fetched from external APIs.

## 5. Data Requirements
The app needs to store user profiles, coin data, coin prices, portfolios, and transaction history in the database. The initial data requirements are minimal, with an expected user count of under 10. However, the design should allow for easy scalability as more users join.

## 6. User Interface
The user interface design is up to the discretion of the frontend development team, with the only requirement being that it should be user-friendly and intuitive.

## 7. Regulatory Requirements
As the app involves trading of simulated coins with game money, there are no specific regulatory requirements.

## 8. Deployment and Maintenance
The app should be designed for deployment on a cloud platform, such as AWS or Google Cloud. The team should also plan for regular maintenance and updates. 

This requirements document aims to provide a comprehensive overview of the necessary features, performance expectations, and user needs for the Cryptocurrency Trading Simulation App. The actual implementation may require minor adjustments or additions to these requirements as development progresses and more information becomes available.