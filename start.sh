if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Hacker-Jr-TG/Nancy-V3.5.git /Nancy-V3.5
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Nancy-V3.5
fi
cd /Nancy-V3.5
pip3 install -U -r requirements.txt
echo "Starting Nancy-V3.5"
python3 bot.py
