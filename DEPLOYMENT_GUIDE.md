# Deployment Guide for Polymarket Bot

## Discord Setup
1. Create a Discord application by visiting the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application** and enter the application name.
3. Navigate to the **Bot** section and click **Add Bot**.
4. Copy the **Token** and save it securely.
5. Under **OAuth2**, ensure the Bot has required permissions, then generate an OAuth2 URL to invite the bot to your server.

## Telegram Setup
1. Open the Telegram app and search for the **BotFather**.
2. Start a chat with BotFather and use the command `/newbot` to create a new bot.
3. Follow the prompts to name your bot and receive a **Token**.
4. Note the Token and the bot’s username.

## Gmail Setup
1. Go to the Google Cloud Console and create a new project.
2. Enable the **Gmail API** for your project.
3. Go to **Credentials** and create OAuth 2.0 credentials.
4. Set the redirect URI to your bot's redirect URI.
5. Download the credentials JSON file.

## Cloud Deployment Options
### DigitalOcean
1. Create a **Droplet** from the [DigitalOcean Console](https://cloud.digitalocean.com/).
2. Choose an OS and plan that fits your needs.
3. SSH into your droplet and install dependencies using `npm` or `yarn`.
4. Clone the repository and configure environment variables.
5. Run your bot with a process manager like `PM2`.

### AWS
1. Create an EC2 instance from the [AWS Management Console](https://aws.amazon.com/console/).
2. Select an appropriate instance type and configure security groups.
3. SSH into your instance and install Node.js.
4. Clone the repository and set up environment variables.
5. Use `systemd` or `PM2` to run your bot in background.

### GitHub Actions
1. Create a `.github/workflows/deploy.yml` file in your repository.
2. Set up the environment variables in GitHub Secrets.
3. Use actions to build and deploy your application automatically on pushes to the main branch.

### Railway
1. Sign in or create an account at [Railway](https://railway.app/).
2. Create a new project and connect your GitHub repository.
3. Set your environment variables in the Railway dashboard.
4. Deploy your bot with a single click.

Ensure all environment variables and tokens are properly set in your hosting environment before running your bot.  
