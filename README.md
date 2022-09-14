# checkup dan backfill
keduanya berhubungan dengan start running bash command dimana <br>
backfill CLI command can run for dates before the start date of the dag but catchup cannot (https://stackoverflow.com/questions/57268540/what-is-the-difference-between-backfill-and-catchup-in-airflow) <br>
untuk lebih jelasnya & mengetahui perbedaan antara catchup dengan backfill maka catchup dibawah ini ubah jd False.<br>
kemudian refresh airflow & lihat beda antara catchup True dg False<br>
kemudian stlh di set False if use docker masuk ke container airflow scheduler dg perintah<br>
docker ps => cari container airflow scheduler lalu copy<br>
docker exec -it {paste id container nya} bash<br>
run backfill dg command -s artinya start_date, -e artinya end_date => airflow dags backfill -s 2022-09-10 -e 2022-19-01 {nama id dag yg ingin diset melalui backfill}<br>
we bisa melihat log "backfill is done", lalu perintah exit<br>
## sumber https://www.youtube.com/watch?v=K9AnJ9_ZAXE
https://www.youtube.com/watch?v=39k2Sz9jZ2c<br>
kubernetes https://www.youtube.com/watch?v=X48VuDVv0do<br>
### ini run & success di linux
<!-- uninstall all package with pip => pip freeze | xargs pip uninstall -y -->