
# Crypto Bank

## Description
Crypto Bank is a decentralized blockchain application that enables secure transactions between users. It allows users to create and manage transactions, mine blocks, and validate the blockchain. With a focus on transparency and security, Crypto Bank ensures the integrity of transaction records in a reliable digital currency platform.

## Features
- Create and manage transactions
- Mine new blocks
- Validate the blockchain
- View transaction history

## Prerequisites
- Python 3.x
- Flask
- Flask-CORS (for cross-origin requests)
- React (for frontend)

## Installation

### Clone the Repository
Clone this repository to your local machine using:
```bash
git clone https://github.com/Yash22222/CryptoBank.git
```

### Navigate to the Project Directory
```bash
cd CryptoBank
```

### Set Up the Backend
1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Set Up the Frontend
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the frontend dependencies:
    ```bash
    npm install
    ```

## Running the Application

### Start the Backend Server
1. Navigate back to the backend directory:
    ```bash
    cd ../backend
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```
   The backend server should start running at `http://127.0.0.1:5000/`.

### Start the Frontend Server
1. Open a new terminal window and navigate to the frontend directory:
    ```bash
    cd CryptoBank/frontend
    ```

2. Start the React application:
    ```bash
    npm start
    ```
   The frontend will be accessible at `http://localhost:3000/`.

## Usage

### API Endpoints
- **GET /**: Welcome message.
- **GET /mine**: Mine a new block.
- **POST /transaction**: Create a new transaction (provide JSON body).
- **GET /chain**: View the entire blockchain.
- **GET /validate**: Validate the blockchain.

### Example Request to Create a Transaction
Use Postman or any REST client to send a POST request to:
```
http://127.0.0.1:5000/transaction
```
With the following JSON body:
```json
{
  "sender": "Alice",
  "recipient": "Bob",
  "amount": 10
}
```

### Output
After successfully creating a transaction or mining a block, you will receive a JSON response indicating the success of the operation. For example, after mining a block, you might see:
```json
{
  "message": "New block mined successfully!",
  "block": {
    "index": 1,
    "transactions": [...],
    "proof": 12345,
    "previous_hash": "abcdef..."
  }
}
```

## Why This Project is Useful
Crypto Bank demonstrates the practical implementation of blockchain technology, showcasing how transactions can be securely processed in a decentralized manner. It provides insights into the workings of cryptocurrencies and the fundamental concepts of blockchain.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Notes
- Be sure to replace any placeholders https://github.com/Yash22222/CryptoBank with your actual project details.
- Adjust any section based on specific features or functionalities you have in your application.
- Add any additional commands or dependencies relevant to your project. 
