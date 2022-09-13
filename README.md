# Lifecycle
ketika dag run di trigger, maka task yg ada didlmnya akan dieksekusi satu persatu.<br>
 setiap task akan berjalan melalui stages yg berbeda mulai dari start sampai complete<br>
 setiap stage mengindikasikan status tertentu dari suatu task instance. contoh ketika task dlm keadaan progress maka statusnya adlh running, ketika task telah selesai maka statusnya success, dst.<br>
 terdpt 11 status stage yg ditampilkan dlm UI. warna dr setiap status stage berbeda beda<br>
stage task yg pertama adlh early dg status dr no_status sampai ke queued (no_status, scheduled, queued), next fase eksekusi task mulai dr status running sampai succes (running, success). if task fail maka akan masuk ke status up_for_retry, upstream_failed, atau up_for_reschedule. selama lifecycle task if kita memaksa scra manual atau skip task maka task akan memasuki status shutdown atau skipped. terakhir status task nya adlh failed
## status/stage lifecycle 
no_status : scheduler created empty task instance (starting)<br>
selanjutnya pd scheduler bisa terjd scheduled (scheduler determined task instance needs to be run), removed (task telah dihapus), upstream_failed (upstream task failed), atau skipped (the task is skipped)<br>
if status scheduler adlh sheduled maka next process is "executor" next "executor" masuk ke dlm task queue sehingga statusnya berubah jd queued. stlh itu worker akan mengeksekusi task stlh free (artinya worker computation resources is not fully occupied) pd tahap ini status dr task adlh running.<br>
stlh stage running, task bisa directed ke stage up_for_reschedule (reschedule task every certain time interval) artinya task akan direschedule setiap selang waktu tertentu (ex file existence every 10 seconds) & kembali ke scheduler<br>
berdsrkan hasil eksekusi tsb maka terdpt 3 stage yg mungkin terjd yaitu success(task berhsl & selesai) / failed (task fail)/ shutdown (task dibatalkan/aborted)<br>
untuk stage failed/shutdown maka task akan diulangi lagi dg masuk ke status up_for_retry (task akan dischedule ulang atau rerun the task) sehingga kembali ke fase / status /stage scheduled tp jika jumlah pengulangannya melebihi batas (ex maks pengulangan adlh 3) maka .....
## proses eksekusi workflow yg diinginkan
no_status => scheduler => scheduled => executor => queued => worker => running
## sumber https://www.youtube.com/watch?v=K9AnJ9_ZAXE
### ini run & success di linux
<!-- uninstall all package with pip => pip freeze | xargs pip uninstall -y -->