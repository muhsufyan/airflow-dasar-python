# Konsep dan dasar
## workflow, dag, task, operator
airflow adlh managemen untuk workflow<br>
workflow adlh sequence of task (sekumpulan tugas yg berurutan/terurut)<br>
sedangkan dlm airflow, workflow diartikan as DAG (directed acyclic graph)<br>
dr namanya saja adlh graf yg tidk membentuk siklus, graf nya bersifat direct (1 arah)<br>
misal ada vertex (tugas) A, stlh task A selesai maka dpt melakukan task B dan C. stlh task B selesai maka dpt melakukan task D. ingat stlh task C maka tdk akan kembali ke task A, atau stlh task D selesai maka tdk akan kembali ke task B atau bahkan ke task A & begitupun stlh task B selesai maka tdk bisa kembali ke mengerjakan task A. Maka dari itu kenapa disbt acyclic<br>
task A upstream ke task B, task B upstream ke task D, task A upstream ke task C<br>
sebaliknya, task D downstream ke task B, task B downstream ke task A, task C downstream ke task A<br>
gambar 1 buah dag<br>
ex A --> B --> D
    |
    |--> C
<br> itulah konsep dari dag. now dag adlh kumpulan semua task yg akan di run, dimana setiap task dapat saling terhubung<br>
lalu ada yg namanya operator. tujuan dari task adlh untuk mencapai "sesuatu yg kita set", metode yg digunakan untuk mencapai "sesuatu itu" disbt dg operator<br>
DAG menggambarkan bagaimana menjlnkan (run) suatu workflow, sedangkan operator menentukan apa yg sbnrnya didpt setelah task beres (mungkin ini seprti return dlm func)<br>
ada banyak operator diantara BashOperator (mengeksekusi perintah bash), PythonOperator (mengeksekusi kode python), CustomisedOperator<br>
setiap task akan menerapkan operator jd pd kasus diatas misalnya, task A menerapkan operator PythonOperator, task B menerapkan operator BashOperator, dst.

## execution date, task instance, dag run
execution data adlh logical date & time which the DAG run, & its task instances, and dag run for<br>
ex kita punya 3 dag sprti diatas dimana setiap dag akan di run pd 2023-01-01, 2023-01-02,2023-01-03<br>
task instance is a run of a task at a specific point of time (execution_date)<br>
task instance => (setiap task with operator) + hari ini (ex 2022-09-12)<br>
dag run is an instantiation of a DAG, containing task instances that run for a specific execution_data<br>
DAG run => DAG + hari ini (ex 2022-09-12)
## sumber https://www.youtube.com/watch?v=K9AnJ9_ZAXE
### ini run & success di linux
<!-- uninstall all package with pip => pip freeze | xargs pip uninstall -y -->