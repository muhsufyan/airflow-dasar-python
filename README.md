# Basic Architecture
lihat gambar arsitektur https://airflow.apache.org/docs/apache-airflow/2.0.1/concepts.html<br>
data engineer (kita) memonitoring proses ETL, config file/buat setup lewat Airflow.cfg (setup tipe db, tipe operator, dag, dll)<br>
kita membuat & memanage DAG melalui UI via web server<br>
kita as author, melalui DAG dpt melihat scheduler & worker yg mengubah status task selama lifecycle berlangsung.<br>
apart from that(selain itu),ada komponen yg disbt as executor. executor ini akan melanjutkan pembaruan(update) dan mengambil(retrieve) info dags<br>
Executor dpt berupa Local atau Sequence<br>
ke4 komponen tsb (web server, scheduler, executor, Executor, dan workers) akan terkoneksi ke db<br>
ada banyak db yg dpt dipilih mulai dr sql (mysql, postgre, dll), nosql, dll. db ini disbt as metadata db
## sumber https://www.youtube.com/watch?v=K9AnJ9_ZAXE
### ini run & success di linux
<!-- uninstall all package with pip => pip freeze | xargs pip uninstall -y -->