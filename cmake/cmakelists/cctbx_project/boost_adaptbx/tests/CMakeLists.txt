add_python_library ( boost_adaptbx_python_streambuf_test_ext
            python_streambuf_test_ext.cpp )

add_executable(tst_optional_copy_2 tst_optional_copy.cpp)
set_target_properties(tst_optional_copy_2 PROPERTIES     OUTPUT_NAME tst_optional_copy)
add_test(NAME tst_optional_copy_2 COMMAND tst_optional_copy_2)

