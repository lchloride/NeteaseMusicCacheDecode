# 网易云音乐缓存重命名

## 功能
- 重命名 mp3 文件，查找 song id 对应的 `歌手名` 与 `歌曲名`，并将文件重命名为 `歌手名 - 歌曲名.mp3`
  ```md
  From: source path/<song id>-<bite rate>-<random number>.mp3
  To: dist path/<artist name> - <song title>.mp3
  ```
## 使用说明示例
- 在 Ubuntu 上使用网易云音乐的客户端，其缓存直接是 mp3 文件，缓存在 `~/.cache/netease-cloud-music/CachedSongs/`
  ```shell
  $ ls ~/.cache/netease-cloud-music/CachedSongs/ -1
  1609689-320-b70d1d38edd3f443bc503f592fc440ed.mp3
  25638306-320-3d42ddad5384518bbbf8bc68fff4cdfa.mp3
  4254253-128-1fb4ae7055ea4ceb36862f6228e61aa4.mp3
  441116287-128-0d15579de47acbe4c8177e54ba43bf4b.mp3
  ```
- 因此主要需要的是重命名，使用如下
  ```shell
  $ python netease_rename.py
  source = ~/.cache/netease-cloud-music/CachedSongs, dist = ~/output_music
  song_id = 25638306, tt.tag title = ありがとう…, artist = KOKIA, album = ありがとう…, album_artist = KOKIA
  song_id = 441116287, tt.tag title = 茜さす, artist = Aimer, album = 茜さす/everlasting snow, album_artist = Aimer
  song_id = 4254253, tt.tag title = Mustang cabriolet, artist = Paris Brune, album = L’œil du cyclone, album_artist = Paris Brune
  song_id = 1609689, tt.tag title = Vale Of Tears, artist = Jay Clifford, album = Silver Tomb For The Kingfisher, album_artist = Jay Clifford
  ```
- 输出
  ```shell
  $ ls ~/output_music/ -1
  'Aimer - 茜さす.mp3'
  'Jay Clifford - Vale Of Tears.mp3'
  'KOKIA - ありがとう….mp3'
  'Paris Brune - Mustang cabriolet.mp3'
  ```
## 参数
- `--dist_path` 输出路径，默认 `$HOME/output_music`
- `--source_path` 输入文件夹路径，缓存文件地址，默认 `$HOME/.cache/netease-cloud-music/CachedSongs`
- `--help` 帮助信息
## 依赖
- **eyed3** mp3 文件属性赋值，如 title / artist / album / album_artist
  ```shell
  $ pip install eyed3
  ```
- **requests** 网页请求
  ```shell
  $ pip install requests
  ```
- **shutil** 文件复制
  ```shell
  $ pip install shutil
  ```
