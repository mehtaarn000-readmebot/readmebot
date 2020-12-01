# $1 = git url of original repository
# $2 = git url of forked repository
# $3 = name of owner
# $4 = description
# $5 = main branch of original repository
# $6 = name of repository

mkdir new_dir
cd new_dir
git init
git remote add origin $1
git clone $1
cd $6
hub fork
touch README.md
cp ~/Desktop/READMEBot/utils/COMMIT_MESSAGE.md COMMIT_MESSAGE.md
READMEFILE=$(cat << EOM
# $3

$4

## Installation
`Some installation methods`

## Dependancies
`Some dependancies`

## Usage
`Some usage methods`

## Contributing
`How to contribute`
EOM
)
echo $4 >> README.md
sleep 15
git remote set-url origin $2
git pull origin master --allow-unrelated-histories
sleep 10
git add README.md
git commit -m "Add README.md"
sleep 2
git push -u origin master
sleep 10
hub pull-request --file utils/COMMIT_MESSAGE.md -b $3:$5 -h mehtaarn000-readmebot:master -f
sleep 6
hub delete -y $6
rm -rf new_dir