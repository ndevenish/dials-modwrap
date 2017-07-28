add_library ( iotbx_xplor 
            map_reader.cpp
            map_writer.cpp )
target_link_libraries(iotbx_xplor iotbx)

add_subdirectory(boost_python)
