#!/bin/bash
if [ "$(cat /etc/resolv.conf)" = "$(cat ~/.config/dns/opendns)" ]
then
    cat ~/.config/dns/shekan > ~/.config/dns/resolv.conf;sudo cp ~/.config/dns/resolv.conf /etc/resolv.conf && echo switched to shekan
else
    cat ~/.config/dns/opendns > ~/.config/dns/resolv.conf;sudo cp ~/.config/dns/resolv.conf /etc/resolv.conf && echo switched to opendns
fi;
