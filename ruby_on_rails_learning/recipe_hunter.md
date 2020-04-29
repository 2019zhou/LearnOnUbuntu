# 大作业遇到的问题

## rails 部署
1. rails 部署 can't find gem bundler (>= 0.a) with executable bundle
- 解决方案 gem uninstall bundler  gem install bundler --version '1.17.2'
- tail Gemlock 中不一致的问题 

2. warining:The dependency tzinfo-data (>= 0) will be unused by any of the platforms Bundler is installing for. Bundler is installing for ruby but the dependency is only for x86-mingw32, x86-mswin32, x64-mingw32, java. To add those platforms to the bundle, run `bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java`.
- 原因This gem is unnecessary for apps that will be running on Ubuntu (or any Unix-based system) and can be safely removed from the gemfile unless your rails app is running on a Windows machine. 直接忽视就可以了

