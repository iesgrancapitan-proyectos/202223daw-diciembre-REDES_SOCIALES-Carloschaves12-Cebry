# define a function to check if a package is installed
check_installed() {
    echo "Checking for $1..."
    echo ''
    package --version
    if [ $? -eq 0 ]; then
        echo "$1 is installed"
    else
        echo "$1 is not installed"
        echo "installing $1..."
         sudo apt install $1 -y

        if [ $? -eq 0 ]; then
            echo "$1 is installed"
        else
            echo "$1 could not be installed"
            exit 1
        fi

    fi
        echo '\n'
}

check_python_package() {
    echo "Checking for $1..."
    echo ''

    pip3 show $1
    if [ $? -eq 0 ]; then
        echo "$1 is installed"
    else
        echo "$1 is not installed"
        echo "installing $1..."
        pip3 install $1

        if [ $? -eq 0 ]; then
            echo "$1 is installed"
        else
            echo "$1 could not be installed"
            exit 1
        fi
    fi

    echo '\n'
}

# check usage 'sh deploy.sh'
if [ $# != 0 ]; then
    echo "Usage: sh deploy.sh"
    exit 1
fi

# # check if the script is running as root
# if [ $(id -u) != "0" ]; then
#     echo "Error: You must be root to run this script, please use root"
#     exit 1
# fi

# # update system
# echo "Updating system"
# echo ''
# sudo apt update && sudo apt upgrade -y
# echo '\n'
# echo "System updated"
echo ''
echo "Checking for dependencies..."
# check if 'git' is installed
check_installed git

# check if 'at' is installed
check_installed at

# check if 'python3' is installed
check_installed python3

# check if 'pip3' is installed
check_installed python3-pip
echo "All dependencies are installed"
echo '\n'
echo "Installing python3 dependencies"
echo ''

# check if 'python-dotenv' is installed with pip3
check_python_package python-dotenv

# check  if 'tweepy' is installed
check_python_package tweepy

# check if 'requests' is installed
check_python_package requests


echo "All python dependencies are installed"