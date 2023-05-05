import os


class UserGroupSetup:
    def __init__(self, root_dir="/", config_dir="/"):
        self.root_dir = root_dir
        self.config_dir = config_dir
        os.system("sudo groupadd mediacenter -g 13000")

    def create_config_dir(self, service_name):
        os.system(
            f"sudo mkdir -p {self.config_dir}/{service_name}-config"
            f" ; sudo chown -vR {service_name}:mediacenter {self.config_dir}/{service_name}-config"
            f" ; sudo chown -v $(id -u):mediacenter {self.config_dir}"
        )

    def sonarr(self):
        os.system(
            '/bin/bash -c "sudo useradd sonarr -u 13001'
            " ; sudo mkdir -pv "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/tv -m 775"
            " ; sudo chown -vR sonarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/tv"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
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
            " ; sudo chown -vR radarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/movies"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
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
            " ; sudo chown -vR lidarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/music"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
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
            " ; sudo chown -vR readarr:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/books"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
            + self.root_dir
            + '/data/{media,torrents,usenet}"'
        )
        self.create_config_dir("readarr")
        os.system("sudo usermod -a -G mediacenter readarr")

    def calibre(self):
        os.system("sudo useradd calibre -u 13013")
        self.create_config_dir("calibre")
        os.system("sudo usermod -a -G mediacenter calibre")

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
            " ; sudo chown -vR mylar:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/comics"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
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
            " ; sudo chown -vR audiobookshelf:mediacenter "
            + self.root_dir
            + "/data/{media,torrents,usenet/complete}/audiobooks"
            " ; sudo chown -v $(id -u):mediacenter " + self.root_dir + "/data"
            " ; sudo chown -v $(id -u):mediacenter "
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
            " ; sudo chown -vR sabnzbd:mediacenter"
            f' {self.root_dir}/data/usenet/incomplete"'
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
        os.system(f"sudo mkdir -p {self.config_dir}/jellyfin-config")
        os.system(f"sudo chown -vR {self.config_dir}/jellyfin-config")
