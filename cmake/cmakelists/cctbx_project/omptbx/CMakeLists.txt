project(omptbx)

add_library ( omptbx 
            stubs.cpp )
target_include_directories(omptbx PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/${CMAKE_CURRENT_SOURCE_DIR}/..)


add_python_library ( omptbx_ext
            ext.cpp )
target_link_libraries(omptbx_ext omptbx)

