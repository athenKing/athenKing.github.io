---
layout: post
title:  "Installation recording of ABY"
<!-- date:  -->
categories: jekyll update
---

brew install openssl

cmake -DABY_BUILD_EXE=On -DCMAKE_BUILD_TYPE=Debug -DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2l/ ..


in sharing.cpp, make these modifications:

add inlucdes:

#include <boost/filesystem.hpp>
#include <boost/system/error_code.hpp>

namespace filesystem = boost::filesystem;


	boost::system::error_code ec;

in boolsharing.cpp, change filesystem to boost::filesystem

namespace filesystem = boost::filesystem;



In src/abycore directory, change CMakeLists.txt by line 38

make modifications like this:
 	find_package(Boost COMPONENTS system filesystem REQUIRED)

	target_link_libraries(aby
	#	PRIVATE stdc++fs
	  PRIVATE ${Boost_FILESYSTEM_LIBRARY}
	  PRIVATE ${Boost_SYSTEM_LIBRARY}
	)
