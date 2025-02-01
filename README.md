# MoveAIID – AI-Enhanced Decentralized Identity & Reputation Platform

MoveAIID is a decentralized identity and reputation platform built on the Movement Network. It leverages the power of Move smart contracts, decentralized identifiers (DIDs) following the MoveDID protocol, and AI agents (via Fleek’s Eliza Framework) to enable users to securely manage their on-chain profiles and generate real-time reputation scores. This platform not only empowers users with complete control over their digital identity but also provides developers with robust tools for integration into DeFi, social dApps, and other Web3 services.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact & Support](#contact)

## Overview
MoveAIID combines cutting-edge decentralized identity (DID) protocols with AI-driven reputation analytics to create a next-generation digital identity platform on the Movement Network. Users can create and update their on-chain profiles, while an integrated AI agent continuously analyzes on-chain behavior, transaction history, and (optionally) off-chain data to produce dynamic reputation scores. These scores can then be used for:

- **Authentication and Access Control:** Granting users access to exclusive dApps, investment opportunities, or community privileges.
- **Risk Assessment:** Helping DeFi protocols or other financial services evaluate user credibility.
- **Social and Community Engagement:** Rewarding users with higher reputation scores through airdrops or enhanced functionalities.

## Key Features
### Decentralized Identity (DID) Management
- Utilize the MoveDID protocol to create, update, and manage secure on-chain digital identities.
- On-chain bio smart contracts allow users to register personal details (name, bio, social links).

### AI-Powered Reputation Engine
- Integrates with Fleek’s Eliza Framework to analyze on-chain data (transaction history, NFT holdings, DeFi interactions) and generate reputation scores.
- Provides personalized recommendations and alerts to help users improve their digital footprint.

### Developer-Friendly Interface
- A React/TypeScript frontend with robust wallet integration using the Aptos Wallet Adapter.
- GraphQL integration with Movement’s Indexer API for real-time on-chain data retrieval.

### Modular and Scalable
- Built using Movement smart contracts (Move language) ensuring high performance, security, and scalability.
- Seamless integration with other Web3 applications, opening up opportunities for DeFi, social dApps, and more.

### Secure and Transparent
- Leverages Movement’s Fast Finality Settlement and robust validator network.
- All identity and reputation data is stored immutably on-chain, ensuring transparency and trust.

## Architecture
MoveAIID is designed with a modular architecture that integrates several key components:

### Onchain Smart Contracts (Move)
- **MoveDID & Onchain Bio Modules:** Manage decentralized identity information and profile details.
- **Reputation Smart Contracts:** Interface with the AI agent to record reputation scores and update user profiles.

### AI Agent (Fleek Eliza Framework)
- An AI-driven service that analyzes on-chain data retrieved via the GraphQL API.
- Generates reputation scores and offers improvement recommendations.

### Frontend (React/TypeScript)
- User dashboard for profile management, reputation score display, and AI recommendations.
- Wallet integration (via Aptos Wallet Adapter) for secure authentication and transaction signing.

### Indexer & Data Services
- Utilizes Movement’s Indexer API (GraphQL) to fetch real-time and historical on-chain data.
- Provides data for the AI agent and frontend display.

### Backend & Orchestration
- Deployment and integration scripts using Movement CLI.
- Server-side orchestration on a Hetzner instance for hosting and additional API services if needed.

## Tech Stack
- **Smart Contracts:** Move (Movement Network)
- **Frontend:** React, TypeScript, Ant Design (for wallet selector/UI components)
- **Wallet Integration:** `@aptos-labs/wallet-adapter-react`, `petra-plugin-wallet-adapter`
- **AI Agent:** Fleek’s Eliza Framework (or similar AI SaaS service)
- **Data Access:** GraphQL (Movement Indexer API)
- **Deployment & Infrastructure:** Movement CLI, Docker, Ansible, Hetzner cloud servers

## Getting Started
### Prerequisites
- Movement CLI: [Installation Guide](https://movementlabs.xyz)
- Node.js & npm/yarn: Recommended Node.js version LTS
- Git: For version control and repository cloning
- Docker & Ansible: (For deployment on Hetzner server)
- Hetzner Server Access: SSH key-based authentication to your remote server

### Local Development Setup

#### Clone the Repository:
```bash
git clone https://github.com/<your-github-username>/moveaiid.git
cd moveaiid
```
#### Directory Structure:
```bash
moveaiid/
├── contracts/             # Move smart contracts (Move modules)
├── client/                # React frontend application
├── docs/                  # Documentation & diagrams
├── deployment/            # Deployment scripts (Ansible, Docker, etc.)
├── assets/                # Logos, diagrams, and images
└── README.md              # This file
```
### Smart Contract Deployment

#### Navigate to the Contracts Folder:
```bash
cd contracts
```
#### Initialize Movement CLI and Configure Profile:
```bash
movement init --skip-faucet
# When prompted, choose custom network endpoints:
# RPC/Rest Endpoint: https://aptos.testnet.porto.movementlabs.xyz/v1
# Faucet Endpoint: https://faucet.testnet.porto.movementlabs.xyz/
```
#### Create and Scaffold Your Move Project:
```bash
movement move init --name moveaiid_onchain
```
#### Implement the Smart Contracts:
- Develop your Move modules (e.g., onchain_did.move, reputation.move) in the sources/ folder.
- Update the Move.toml file with your account addresses and dependencies (such as MoveDID).
#### Compile, Test, and Publish:
```bash
movement move compile --named-addresses moveaiid_onchain=default
movement move test --named-addresses moveaiid_onchain=default
movement move publish --named-addresses moveaiid_onchain=default
```

### Frontend Setup

#### Navigate to the Client Folder:
```bash
cd ../client
```
#### Install Dependencies:
```bash
npm install
# or
yarn install
```
#### Configure Environment Variables:
- Create a .env file at the root of the client folder with the following:
```bash
REACT_APP_RPC_URL=https://aptos.testnet.porto.movementlabs.xyz/v1
REACT_APP_FAUCET_URL=https://fund.testnet.porto.movementlabs.xyz
REACT_APP_ONCHAIN_BIO_ADDRESS=<Your_Contract_Address>
REACT_APP_INDEXER_GRAPHQL_URL=https://indexer.testnet.porto.movementnetwork.xyz/v1/graphql
```
#### Run the Development Server:
```bash
npm start
# or
yarn start
```
Your frontend should now be available at http://localhost:3000.

## Deployment
### Deploying on the Movement Network
- #### Movement CLI:
Follow the steps outlined in the Smart Contract Deployment section to publish your Move modules to the Movement Testnet/Mainnet.
- #### Onchain Configuration:
Ensure that your configuration files (e.g., .movement/config.yaml and Move.toml) are correctly updated with your account and network details.

## Usage
### User Onboarding
- Users connect their Aptos wallet using the integrated wallet adapter.
- They can register and update their on-chain bio and DID information.

### Reputation Dashboard
- View real-time reputation scores calculated by the AI agent.
- Receive personalized recommendations to improve their digital footprint.

### Integration with Other dApps
- Developers can utilize MoveAIID’s APIs and smart contracts to integrate decentralized identity and reputation into their own projects.

## Contributing
We welcome contributions from the community! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Create a new Pull Request.

For any major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

### Contact
For any questions or contributions, please contact me from here:
philosophyfactss@gmail.com

### Socials:
Discord: kresna6773
Telegram: @lesnacrex  

Empower your digital identity. Revolutionize reputation management. Welcome to MoveAIID!
