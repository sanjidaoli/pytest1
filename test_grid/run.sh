for i in 'adb devices |grep 'devices' |awk '{print $1}'
do
    echo $1
    udid = $1 pytest test_contact.py
done
