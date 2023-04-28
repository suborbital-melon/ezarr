import os


class UserGroupSetup:
    def __init__(self, root_dir="/"):
        self.root_dir = root_dir
        os.system("sudo groupadd mediacenter -g 13000")
        os.system("export UID=$(id -u)")

    def create_config_dir(self, service_name):
        os.system(
            f"sudo mkdir -p {self.root_dir}/docker/{service_name}-config"
            f" ; sudo chown -R {service_name}:mediacenter {self.root_dir}/docker/{service_name}-config"
            f" ; sudo chown $(id -u):mediacenter {self.root_dir}/docker"
        )

    def sonarr(self):
        os.system(
            '/bin/bash -c "sudo useradd sonarr -u 13001'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/tv -m 775"
            " ; sudo chown -R sonarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/tv"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("sonarr")
        os.system("sudo usermod -a -G mediacenter sonarr")

    def radarr(self):
        os.system(
            '/bin/bash -c "sudo useradd radarr -u 13002'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/movies -m 775"
            " ; sudo chown -R radarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/movies"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("radarr")
        os.system("sudo usermod -a -G mediacenter radarr")

    def lidarr(self):
        os.system(
            '/bin/bash -c "sudo useradd lidarr -u 13003'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/music -m 775"
            " ; sudo chown -R lidarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/music"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("lidarr")
        os.system("sudo usermod -a -G mediacenter lidarr")

    def readarr(self):
        os.system(
            '/bin/bash -c "sudo useradd readarr -u 13004'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/books -m 775"
            " ; sudo chown -R readarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/books"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("readarr")
        os.system("sudo usermod -a -G mediacenter readarr")

    def bazarr(self):
        os.system("sudo useradd bazarr -u 13012")
        self.create_config_dir("bazarr")
        os.system("sudo usermod -a -G mediacenter bazarr")

    def mylar3(self):
        os.system(
            '/bin/bash -c "sudo useradd mylar -u 13005'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/comics -m 775"
            " ; sudo chown -R mylar:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/comics"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("mylar")
        os.system("sudo usermod -a -G mediacenter mylar")

    def audiobookshelf(self):
        os.system(
            '/bin/bash -c "sudo useradd audiobookshelf -u 13009'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/audiobooks -m 775"
            " ; sudo chown -R audiobookshelf:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/audiobooks"
            " ; sudo chown $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("audiobookshelf")
        os.system("sudo usermod -a -G mediacenter audiobookshelf")

    def prowlarr(self):
        os.system("sudo useradd prowlarr -u 13006")
        self.create_config_dir("prowlarr")
        os.system("sudo usermod -a -G mediacenter prowlarr")

    def qbittorrent(self):
        os.system("sudo useradd qbittorrent -u 13007")
        os.system("sudo usermod -a -G mediacenter qbittorrent")

    def sabnzbd(self):
        os.system(
            '/bin/bash -c "sudo useradd sabnzbd -u 13011'
            f" ; sudo mkdir -pv {self.root_dir}/data/usenet/incomplete -m 775"
            " ; sudo chown -R sabnzbd:mediacenter"
            f"{self.root_dir}/data/usenet/incomplete"
        )
        os.system("sudo usermod -a -G mediacenter sabnzbd")
        self.create_config_dir("sabnzbd")

    def overseerr(self):
        os.system("sudo useradd overseerr -u 13009")
        self.create_config_dir("overseerr")
        os.system("sudo usermod -a -G mediacenter overseerr")

    def jellyseerr(self):
        os.system("sudo useradd jellyseerr -u 13010")
        self.create_config_dir("jellyseerr")
        os.system("sudo usermod -a -G mediacenter jellyseerr")

    def jellyfin(self):
        os.system(f"sudo mkdir -p {self.root_dir}/docker/jellyfin-config")
