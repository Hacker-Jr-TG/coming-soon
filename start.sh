echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Hacker-Jr-TG/coming-soon.git /coming-soon
cd /coming-soon
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
