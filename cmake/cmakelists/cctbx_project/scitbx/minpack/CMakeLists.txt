add_library ( scitbx_minpack 
            raw.cpp )
target_link_libraries(scitbx_minpack scitbx)

add_python_library ( scitbx_minpack_ext
            ext.cpp )
target_link_libraries(scitbx_minpack_ext scitbx_minpack scitbx_boost_python)

