project(spotfinder)

add_library ( spotfinder 
            core_toolbox/spot.cpp
            core_toolbox/libdistl.cpp
            core_toolbox/hough.cpp
            core_toolbox/distl.cpp
            core_toolbox/spotfilter.cpp )
target_include_directories(spotfinder PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/${CMAKE_CURRENT_SOURCE_DIR}/..)


add_python_library ( spotfinder_distltbx_ext
            core_toolbox/boost_python/distltbx_ext.cpp
            diffraction/geometry.cpp )
target_link_libraries(spotfinder_distltbx_ext spotfinder omptbx scitbx_boost_python)

add_subdirectory(array_family)
add_subdirectory(core_toolbox)
add_subdirectory(dxtbx_toolbox)
