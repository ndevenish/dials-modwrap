add_library ( dxtbxspotfinder 
            libdistl.cpp
            distl.cpp )
target_link_libraries(dxtbxspotfinder spotfinder)

add_python_library ( spotfinder_dxtbx_ext
            ext.cpp )
target_link_libraries(spotfinder_dxtbx_ext spotfinder omptbx dxtbxspotfinder scitbx_boost_python)

