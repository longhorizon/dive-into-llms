> Bản dịch tiếng Việt · nguồn: [stega.pdf](../../documents/chapter7/stega.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc.

## Trang 1

**Giấu tin trong mô hình lớn**

张玉龙

## Trang 2

**Ứng dụng của mô hình lớn trong truyền thông an toàn**

Giấu tin (Steganography) là một kỹ thuật ẩn giấu thông tin, với mục đích cốt lõi là nhúng thông tin vào nhiều loại vật mang (carrier) khác nhau (như ảnh số, âm thanh, video hoặc văn bản) nhằm truyền thông ẩn. Giấu tin khác với mã hóa: nó không chỉ che giấu nội dung thông tin mà còn che giấu cả sự tồn tại của hành vi truyền tin. Kỹ thuật này lợi dụng đặc tính hệ thống tri giác của con người không nhạy cảm với một số loại thông tin, để giấu thông tin mật vào phần thông tin dư thừa (redundancy) của vật mang số, khiến thông tin bề ngoài trông không khác gì vật mang thông thường, do đó kẻ tấn công khó phát hiện. Ứng dụng của giấu tin bao gồm nhưng không giới hạn ở truyền tin ẩn, bảo vệ bản quyền v.v. Cùng với sự phát triển của công nghệ, giấu tin ngày càng trở nên quan trọng trong các lĩnh vực quân sự, thương mại..., đồng thời cũng tạo điều kiện cho các hành vi xấu như hoạt động gián điệp, khủng bố.

## Trang 3

**Ý nghĩa của giấu tin**

Nói một cách đơn giản, giấu tin là một phương pháp truyền thông tin an toàn khác với mật mã học.

Mật mã "mã hóa" văn bản rõ (plaintext), khiến nội dung thông tin cần truyền không bị bên trung gian lấy được; nhưng vật mang của thông tin có thể bị bên trung gian phát hiện và chiếm được, từ đó làm giả mạo, chặn đứng việc truyền tin.

Giấu tin thì "giấu giấu" chính sự kiện truyền tin, ẩn nội dung thông tin cần truyền ngay trên kênh công khai, ngụy trang thành nội dung thông thường; mục tiêu là chỉ người nhận thông tin mới phát hiện được thông tin được giấu, còn bên trung gian thì không.

Ví dụ giấu tin đơn giản trong đời sống: thơ tàng đầu (chữ đầu các câu ghép thành một thông điệp), mẩu giấy kẹp trong sách v.v.

Công nghệ phái sinh downstream của giấu tin: watermark — có thể hiểu là một dạng giấu tin chú trọng hơn tính bền vững (robustness), sẵn sàng để nhiều người phát hiện và giải đọc được thông tin.

## Trang 4

**Ví dụ giấu tin, đối chiếu với mật mã**

Giấu tin (định dạng văn bản):
• Thao tác: điều chỉnh khoảng cách chữ trong tài liệu điện tử (chênh lệch kiểu 0.1pt), màu font (#000000 vs #010101), mã hóa thông tin bằng nhị phân (kiểu "khoảng cách lớn = 1, bình thường = 0") 1.
• Mục tiêu: thông tin được giấu ngay trong văn bản công khai, mắt thường không nhìn thấy.

Mật mã (mật mã Vigenère):
• Thao tác: mã hóa lặp lại với từ khóa (ví dụ khóa "KEY" mã hóa "HELLO" → "RIJVS").
• Mục tiêu: tạo ra văn bản mật mã nhiễu loạn, cần khóa để giải mã 7.
• So sánh:
• Giấu tin: vật mang là tệp bình thường (như hợp đồng), không gây nghi ngờ.
• Mật mã: bản thân ciphertext tố giác "có bí mật", nhưng nội dung được bảo mật.

## Trang 5

**Ví dụ giấu tin**

Giấu tin (LSB ảnh):
• Thao tác: sửa bit có ý nghĩa thấp nhất (LSB) của điểm ảnh, nhúng dữ liệu mật (ví dụ chuỗi nhị phân của một bức ảnh khác). Mắt người không nhận ra khác biệt, nhưng công cụ có thể trích xuất 29.
• Mục tiêu: thông tin giấu trong ảnh thông thường (như ảnh du lịch), qua mặt kiểm duyệt.

Mật mã (AES-256):
• Thao tác: dùng khóa để mã hóa tệp thành nhiễu loạn (ví dụ z.exe → G8x!gF2*...
• Mục tiêu: ngay cả khi tệp bị đánh chặn cũng không thể phá được nội dung.

Use case phối hợp:
• Trước tiên mã hóa dữ liệu nhạy cảm bằng AES;
• sau đó nhúng ciphertext vào LSB của ảnh.
→ Bảo vệ kép: vừa ẩn sự tồn tại (trông như bức ảnh bình thường), vừa ẩn nội dung (cần khóa mới giải mã được)

## Trang 6

**Ví dụ giấu tin**

Giấu tin trong mã QR:
Nguyên lý: thiết kế một mã QR trông hoàn toàn bình thường (trỏ tới một trang web vô hại), nhưng nhúng thêm thông tin ẩn (một URL khác, văn bản, ảnh nhỏ) vào vùng mã sửa lỗi (error correction) hoặc thông qua hoa văn điểm mã được thiết kế kỹ lưỡng. Phần mềm quét mã thông thường chỉ đọc được lớp thông tin bề mặt; cần phần mềm tùy chỉnh mới đọc được lớp ẩn.
Ví dụ: mã QR trên thực đơn nhà hàng — quét mã hiện giới thiệu món ăn (lớp công khai), nhưng quét bằng APP chỉ định thì lấy được mã ưu đãi trong ngày hoặc thông tin nội bộ nhân viên bị ẩn. Mã QR trên áp phich — quét thông thường là giới thiệu sự kiện, lớp ẩn là thiệp mời VIP.
Tình huống đời sống: marketing (trò truy tìm kho báu, mở khóa ưu đãi), truyền thông tin nội bộ (thông báo nhân viên), bảo vệ bản quyền (nhúng thông tin chủ sở hữu vào mã QR công khai).
Điểm cốt lõi: cần hiểu cấu trúc mã QR (đặc biệt là tính dư thừa của mã sửa lỗi), cần công cụ tạo mã QR đặc biệt có hai lớp.

## Trang 7

**Mô hình của giấu tin**

Hiện nay, khi chọn vật mang truyền thông số, giấu tin thường chọn ảnh hoặc video, vì có rất nhiều không gian dư thừa để chèn thông tin. Còn văn bản nếu làm vật mang giấu tin thì độ dư thừa thấp, nhưng nó có ưu điểm linh hoạt, lượng nội dung lớn, dễ dàng nhúng vào các nội dung khác. Lần này chúng ta dùng mô hình ngôn ngữ lớn để giới thiệu giấu tin trong mô hình lớn.
Quy trình của giấu tin (trái) và watermark (phải) mỗi bên được minh họa bằng sơ đồ mô hình hình dưới đây (trong slide).

## Trang 8

**Phân loại giấu tin trong văn bản**

Giấu tin trong văn bản gồm chủ yếu hai loại: dạng sửa đổi và dạng sinh.
Những năm gần đây, cùng với sự phát triển của học sâu và đặc biệt là mô hình lớn, giấu tin văn bản dạng sinh đã trở thành xu hướng chủ đạo.

## Trang 9

**Giấu tin văn bản bằng mô hình lớn 1-3**

Mọi mô hình sinh văn bản đều là dữ liệu "dạng chuỗi" (serialized).
Khi đầu vào là văn cảnh phía trước cùng các tham số, mô hình sẽ trả về một bảng logits dự đoán cho "next token"; trong bảng là các token id xếp từ xác suất cao nhất xuống thấp nhất.
Thông thường, mô hình sẽ chọn ngẫu nhiên một trong n token theo tham số làm token tiếp theo, rồi tiếp tục vòng lặp sinh.
Còn giấu tin dạng sinh, trong quá trình suy luận của mô hình, sẽ can thiệp vào việc mô hình chọn next token theo các quy tắc đã được thiết lập sẵn, từ đó nhúng thông tin muốn giấu vào văn bản được sinh ra ngay trong quá trình suy luận.
[1] Yang, Zhong-Liang, et al. "RNN-stega: Linguistic steganography based on recurrent neural networks." IEEE Transactions on Information Forensics and Security 14.5 (2018): 1280-1295.
[2] Tang, Yifan, et al. "Linguistic Steganalysis via LLMs: Two Modes for Efficient Detection of Strongly Concealed Stego." IEEE Signal Processing Letters (2024).
[3] Yang, Zhong-Liang, et al. "VAE-Stega: linguistic steganography based on variational auto-encoder." IEEE Transactions on Information Forensics and Security 16 (2020): 880-895.

## Trang 10

**Giấu tin văn bản bằng mô hình lớn**

Ví dụ như hình dưới đây (trong slide): giả sử tôi muốn nhúng thông tin mật đã được chuyển thành nhị phân. Tôi có thể mã hóa n token đứng đầu trong danh sách next token mà mô hình trả về mỗi lần. Ví dụ khi tôi nhập "I", 8 token đầu tiên mô hình trả về, xếp theo thứ tự xác suất giảm dần, lần lượt là have(000), am(001), was(010), can(011)... Mỗi token đều tương ứng với một giá trị nhị phân 3 bit. Khi tôi muốn giấu "001", tôi chọn "am" làm next token, rồi tiếp tục vòng lặp phía sau.

## Trang 11

**Giấu tin văn bản bằng mô hình lớn**

Về bản chất, phương pháp này là mã hóa n ứng viên đứng đầu trong danh sách token, xây nên một không gian mã hóa (coding space) ẩn. Khi muốn giải mã thông tin, chỉ cần dùng cùng mô hình, cùng văn cảnh, cùng tham số thì đảm bảo mỗi lần mô hình trả về một không gian mã hóa giống hệt lúc sinh, nhờ đó suy ngược từ token ra luồng thông tin nhị phân ban đầu — ví dụ từ "am" giải mã ngược được 001.

## Trang 12

**Giấu tin văn bản bằng mô hình lớn**

Đương nhiên phương pháp kể trên dùng cách mã hóa rất cố định (mã hóa trực tiếp n token đầu theo thứ tự). Hình dưới đây (trong slide) thực tế sử dụng mã hóa Huffman, nhằm đảm bảo nhúng được càng nhiều thông tin càng tốt, nâng cao tốc độ nhúng.

## Trang 13

**Ý nghĩa và tương lai của giấu tin trong mô hình lớn**

Giấu tin trong mô hình lớn: ưu điểm của việc dùng mô hình lớn để giấu tin là tận dụng được năng lực của mô hình lớn, xuất ra nội dung giấu tin tự nhiên hơn và khó bị phát hiện hơn.
Không gian mã hóa: các phương pháp giấu tin khác nhau phụ thuộc rất nhiều vào cách mã hóa; nếu có cách mới để xây dựng không gian mã hóa thì có thể tạo ra một trường phái giấu tin mới.
Mở rộng giao thoa: bản chất của giấu tin văn bản dạng sinh bằng mô hình lớn là "mã hóa lặp lại trên dữ liệu dạng chuỗi"; kỹ thuật này cũng có thể di thực sang môi giới khác — ví dụ DNA cũng là dữ liệu dạng chuỗi, có thể dùng thiết bị phối hợp với đầu ra của mô hình lớn để giấu tin trên mã hóa DNA, từ đó trong lĩnh vực quân sự có thể thực hiện "giấu thông tin mật trong một chai nước, vài tế bào, vài sợi tóc", đạt trình độ truyền tin ẩn ở mức cực cao.
Watermark cho mô hình lớn: các kỹ thuật watermark cho mô hình lớn hiện có cũng có thể kết hợp và thúc đẩy lẫn nhau với giấu tin. Ví dụ watermark KGW nổi tiếng cũng ràng buộc việc chọn next token trong quá trình suy luận.
An toàn nội dung: công nghệ phản chế của giấu tin là "phân tích giấu tin (Steganalysis)" có thể dùng để đánh giá và sàng lọc, phát hiện nội dung truyền thông mạng. Những kiểu "nói mỉa mai", "băng mạng chửi người" không kích hoạt từ khóa, về bản chất cũng là một dạng "giấu tin", nên cũng có khả năng được các kỹ thuật phát hiện giấu tin tự động bằng trí tuệ nhân tạo phát hiện ra — điều này sẽ có lợi cho việc bảo đảm an toàn không gian mạng của con người trong tương lai.
