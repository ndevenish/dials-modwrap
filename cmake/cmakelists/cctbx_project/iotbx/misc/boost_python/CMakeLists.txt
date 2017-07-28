add_python_library ( iotbx_dtrek_ext
            dtrek_ext.cpp )
target_link_libraries(iotbx_dtrek_ext cctbx)

add_python_library ( iotbx_scalepack_ext
            scalepack_ext.cpp )
target_link_libraries(iotbx_scalepack_ext cctbx)

