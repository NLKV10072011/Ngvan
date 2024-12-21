import streamlit as st

st.title("Đăng ký chương trình")
st.write("Tên học viên: Kiến Văn")

# Thanh tiến trình
bar = st.progress(0)

# Danh sách câu hỏi
cau_hoi = [
    "Tên",
    "Email",
    "Mật khẩu",
    "Nhập lại mật khẩu"
]

# Danh sách lưu trữ câu trả lời
tra_loi = [None] * len(cau_hoi)

# Hiển thị các câu hỏi và lưu câu trả lời
for i in range(len(cau_hoi)):
    if i in [2, 3]:  # Các trường "Mật khẩu" và "Nhập lại mật khẩu"
        tra_loi[i] = st.text_input(cau_hoi[i], type="password")
    else:
        tra_loi[i] = st.text_input(cau_hoi[i], "")

# Tính số câu trả lời đã điền
so_cau_tra_loi = sum(1 for tl in tra_loi if tl != "")

# Cập nhật thanh tiến trình
bar.progress(int((so_cau_tra_loi / len(cau_hoi)) * 100))

# Nút "Tiếp" để xử lý kết quả
if st.button("Tiếp"):
    
    if so_cau_tra_loi == len(cau_hoi):  # Kiểm tra nếu điền đủ thông tin
        
        # Kiểm tra định dạng email
        if tra_loi[1].endswith("@gmail.com"):  # Email phải có đuôi @gmail.com
            
            if tra_loi[2] == tra_loi[3]:  # Kiểm tra mật khẩu khớp
                
                st.success("Bạn đã điền đủ thông tin, email hợp lệ và mật khẩu khớp!")
                st.balloons()

                # Hiển thị câu trả lời
                for i in range(len(cau_hoi)):
                    st.write(f"{cau_hoi[i]}: {tra_loi[i]}")
            else:
                st.error("Mật khẩu và Nhập lại mật khẩu không khớp. Vui lòng kiểm tra lại!")
        else:
            st.error("Email không hợp lệ! Vui lòng nhập email với đuôi @gmail.com.")
    else:
        st.warning("Bạn chưa hoàn thành đủ thông tin!")
