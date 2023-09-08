# Omega Cashier

**Omega Cashier** adalah sebuah program sederhana berbasis Python yang memungkinkan pengguna untuk melakukan proses belanja secara mandiri.
![app_main_menu](https://github.com/yovir/omega_cashier/blob/tix-2/img/app_main_menu.png?raw=true)
Sistem kasir mandiri ini dibangun untuk memenuhi *final project* yang diberikan dalam kelas Python dari [Pacmann](https://pacmann.io).

## Objective

Membuat sistem kasir mandiri dengan fitur:
:white_check_mark:  Membuat ID transaksi.
:white_check_mark: Memasukkan nama item, jumlah item, dan harga item.
:white_check_mark: Melakukan pembaruan item, jumlah item, dan harga item.
:white_check_mark: Menghapus item.
:white_check_mark: Menghapus semua transaksi.
:white_check_mark: Menampilkan keranjang belanja.
:white_check_mark: Memberikan diskon dengan ketentuan.
:white_check_mark: Menerapkan konsep *Modular Code*.
:white_check_mark: Menerapkan prinsip *Clean Code* (PEP8).
:white_check_mark: Membuat dokumentasi *Docstring*.
:white_check_mark: Menerapkan *defense programming* dengan membuat *try, error* di *branching*.
:white_check_mark: Menerapkan fitur tambahan: *currency formatting*, *app banner*, *pretty table*, dan navigasi menu menggunakan *arrow keys* pada *keyboard*, *terminal invokeable Python module*.

## Flowchart
![flowchart_diagram](https://raw.githubusercontent.com/yovir/omega_cashier/main/flowchart_diagram.png)


## Code Snippets Explanation

### Fungsi untuk menambah item `add_item`
```python

def add_item(self, item_name, item_quantity, item_price):
    self.item_name = item_name
    self.item_quantity = item_quantity
    self.item_price = item_price

    # Verifying user input to determine whether it is a positive integer or not.
    if (isinstance(item_quantity, int)
        and item_quantity > 0) and (isinstance(item_price, int) and item_price > 0) and (isinstance(item_name, str)):
        print("\n")
        total_item = item_quantity * item_price
        new_item = pd.DataFrame({
            "Item": [item_name],
            "Quantity": [item_quantity],
            "Price per Item": [item_price],
            "Total": [total_item]
        })
        self.df = pd.concat([self.df, new_item], ignore_index=True)

        self.display_cart()
        print("\n")

    else:
        clear_screen.clear()
   ```

Fungsi `add_item` menerima atribut `item_name` (string), `item_quantity` (integer), dan `item_price` (integer), yang kemudian menguji apakah `item_quantity` dan `item_price` adalah nilai positif. Jika ya, data tersebut akan dimasukkan ke dalam data frame Pandas. Fungsi ini juga melakukan perhitungan `total_item` dengan mengalikan `item_quantity` dengan `item_price`.

### Fungsi untuk menghapus semua transaksi `reset_item`
```python
def reset_item(self):
        # Check if the cart is not empty.
        if self.is_true():
            # Remove all items from the cart's dataframe.
            self.df.drop(self.df.index, inplace=True)
            print("\n")

            # Display a success message.
            print(f"{Back.GREEN}{Fore.BLACK}{self.SUCCESS_MESSAGE}{Style.RESET_ALL}")
            print("All items have been successfully removed from the cart.")

        # Display an error message if the cart is empty
        else:
            print("\n")
            print(f"{Back.YELLOW}{Fore.BLACK}{self.EMPTY_CART_MESSAGE}{Style.RESET_ALL}")
```

Fungsi `reset_item` untuk mengosongkan troli. Fungsi ini memeriksa apakah keranjangnya kosong atau tidak. Jika kosong, semua nilai yang dimasukkan pengguna akan dihapus. Jika tidak, maka akan muncul pesan kesalahan.

### Fungsi untuk menampilkan menu hapus semua transaksi `reset_item_menu`
```python
def reset_item_menu():
    welcome_message.show()
    order.display_cart()
    print("\n")

    # Ask the user whether the user want to remove item again.
    if not cutie.prompt_yes_or_no("Do you want to reset the cart?", enter_empty_confirms=False):
        # Show welcome message and current cart.
        welcome_message.show()
        order.display_cart()

        # Clear the screen then go back to main menu.
        clear_screen.clear()
        main()
    
    else:
        order.reset_item()
        print("\n")
        input(ENTER_TO_CONTINUE ).lower().startswith(" ")
        clear_screen.clear()
        main()
```

Fungsi `reset_item_menu` digunakan untuk menampilkan menu interaktif sehingga pengguna dapat menentukan apakah ingin menghapus semua transaksi atau tidak. Apabila pengguna tidak jadi menghapus semua transaksi maka program kembali ke menu awal.

## Test Case

### Test #1 - Add items into cart
![Add items](https://github.com/yovir/omega_cashier/blob/tix-2/img/app_1_test_case.png?raw=true)

### Test #2 - Remove an item

![Remove an item](https://github.com/yovir/omega_cashier/blob/tix-2/img/app_2_test_case.png?raw=true)

### Test #3 - Reset cart
![Reset cart](https://github.com/yovir/omega_cashier/blob/tix-2/img/app_3_test_case.png?raw=true)


### Test 4 - Checkout cart
![Checkout cart](https://github.com/yovir/omega_cashier/blob/tix-2/img/app_4_test_case.png?raw=true)


## Installation
1. Clone this repository.
```bash
git clone https://github.com/yovir/omega_cashier
```
2. Navigate to the folder you just cloned.
```bash
cd omega_cashier
```
3. Install the module.
```bash
pip3 install -e .
```
4. Run the program.
```bash
cashier
```

## Kesimpulan

Program mampu beroperasi sesuai alur dan persyaratan yang diinginkan. Secara keseluruhan, program mampu memfasilitasi proses belanja mandiri dengan menggunakan fitur-fitur sederhana yang telah diimplementasikan.

## Saran perbaikan

1. Belum terintegrasi dengan *database* untuk proses penyimpanan data transaksi.
2. Belum tersedia fitur katalog barang sehingga pengguna tidak perlu mengisi rincian barang secara manual.
