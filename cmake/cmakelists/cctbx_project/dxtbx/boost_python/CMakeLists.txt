add_python_library ( dxtbx_ext
            to_ewald_sphere_helpers.cc
            ext.cpp )
target_link_libraries(dxtbx_ext cbf TIFF::TIFF)

