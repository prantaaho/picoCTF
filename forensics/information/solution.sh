head -10 cat.jpg | grep -aoE "resource='.*'" | cut -d= -f 2 | tr -d \' | base64 -d -
