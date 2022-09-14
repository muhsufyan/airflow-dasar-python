# scheduler with cron expression
saat pembuatan dag pd param schedule_interval dpt diisi datetime.timedelta atau cron expression (INGAT KE2NYA HRS DLM BENTUK STRING)<br>
untuk mengetahui cron expression link https://crontab.guru/ . intinya adlh pengaturan schedul waktu, ex pd airflow scheduler kode akan dieksekusi setiap hari jumat jam 23:00, format cron nya adlh 0 23 * * 5 atau bisa juga 0 23 * * Fri<br>
untuk hari bisa gunakan 3 huruf pertama dlm bahasa inggris. untuk setiap hari yg dipilih ex hari senin, kamis dan sabtu => 0 23 * * Mon,Thu,Sat<br>
untuk setiap hari rabu sampai jumat (artinya rabu, kamis, & jumat) => 0 23 * * Tue-Fri
sblm"nya kita gunakan non standard cron expression yaitu @daily (https://crontab.guru/daily)
## sumber https://www.youtube.com/watch?v=K9AnJ9_ZAXE
https://www.youtube.com/watch?v=39k2Sz9jZ2c<br>
kubernetes https://www.youtube.com/watch?v=X48VuDVv0do<br>
### ini run & success di linux
<!-- uninstall all package with pip => pip freeze | xargs pip uninstall -y -->