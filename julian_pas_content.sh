cat $1 | sed 's/	/    /gi' | sed 's/;[[:space:]]*/;/g' | sed '/^[[:space:]]*$/d' | sed 's/{[[:space:]]*$/{/g' | sed 's/}[[:space:]]*$/}/g' > 71iQXbs9Clc04iGD91bP
rm -r $1; mv 71iQXbs9Clc04iGD91bP $1
