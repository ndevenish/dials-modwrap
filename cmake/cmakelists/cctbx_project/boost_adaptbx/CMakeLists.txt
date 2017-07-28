project(boost_adaptbx)

add_library( boost_adaptbx INTERFACE )
target_include_directories(boost_adaptbx INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( boost_optional_ext
            optional_ext.cpp )

add_python_library ( boost_python_hybrid_times_ext
            hybrid_times_ext.cpp )

add_python_library ( boost_python_meta_ext
            meta_ext.cpp )

add_python_library ( boost_rational_ext
            rational_ext.cpp )

add_python_library ( boost_tuple_ext
            tuple_ext.cpp )

add_python_library ( std_pair_ext
            std_pair_ext.cpp )

add_subdirectory(graph)
add_subdirectory(tests)
