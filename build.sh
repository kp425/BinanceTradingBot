# Clones env files stored in a private github repo
function get_env_files() {
    
    remote_url=$1
    env_folder=$2

    echo $remote_url
    echo $env_folder

    current="$(dirname "$BASH_SOURCE")"
    echo $current

    tmp_folder="$current/temp"
    echo $tmp_folder
    mkdir $tmp_folder
    git clone $remote_url $tmp_folder

    # env_folder="BinanceBotEnvs"
    
    src="$tmp_folder/$env_folder/."
    dest="$current/env"

    echo $src
    echo $dest

    cp -a $src $dest
    rm -r "$current/temp"
}


get_env_files $1 $2

current="$(dirname "$BASH_SOURCE")"
pip install -r "$current/requirements.txt"


