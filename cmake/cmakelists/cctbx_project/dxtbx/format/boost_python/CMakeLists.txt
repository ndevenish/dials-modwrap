add_python_library ( dxtbx_format_image_ext
            image_ext.cc )
target_link_libraries(dxtbx_format_image_ext cbf TIFF::TIFF HDF5::HDF5)

add_python_library ( dxtbx_format_nexus_ext
            nexus_ext.cc )
target_link_libraries(dxtbx_format_nexus_ext cbf TIFF::TIFF HDF5::HDF5)

