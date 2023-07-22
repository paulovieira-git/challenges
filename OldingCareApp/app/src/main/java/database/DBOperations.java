package database;


import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.provider.BaseColumns;

import java.util.ArrayList;
import java.util.List;

public class DBOperations {
    FeedReaderDbHelper dbHelper;
    Context context;
    public DBOperations(Context context){
        context=this.context;
        dbHelper = new FeedReaderDbHelper(context);
    }

    public void setDB(FeedReaderContract.FeedEntry fd, String title, String subtitle) {

        FeedReaderDbHelper dbHelper = new FeedReaderDbHelper(context);
        // Gets the data repository in write mode
        SQLiteDatabase db = dbHelper.getWritableDatabase();


        // Create a new map of values, where column names are the keys
        ContentValues values = new ContentValues();
        values.put(fd.COLUMN_NAME_TITLE, title);
        values.put(fd.COLUMN_NAME_SUBTITLE, subtitle);

        // Insert the new row, returning the primary key value of the new row
        long newRowId = db.insert(fd.TABLE_NAME, null, values);
    }
    public List getDB(BaseColumns bc, FeedReaderContract.FeedEntry fd){
        SQLiteDatabase db = dbHelper.getReadableDatabase();

// Define a projection that specifies which columns from the database
// you will actually use after this query.
        String[] projection = {
                bc._ID,
                fd.COLUMN_NAME_TITLE,
                fd.COLUMN_NAME_SUBTITLE
        };

// Filter results WHERE "title" = 'My Title'
        String selection = fd.COLUMN_NAME_TITLE + " = ?";
        String[] selectionArgs = { "My Title" };

// How you want the results sorted in the resulting Cursor
        String sortOrder =
                fd.COLUMN_NAME_SUBTITLE + " DESC";

        Cursor cursor = db.query(
                fd.TABLE_NAME,   // The table to query
                projection,             // The array of columns to return (pass null to get all)
                selection,              // The columns for the WHERE clause
                selectionArgs,          // The values for the WHERE clause
                null,                   // don't group the rows
                null,                   // don't filter by row groups
                sortOrder               // The sort order
        );
        List itemIds = new ArrayList<>();
        while(cursor.moveToNext()) {
            long itemId = cursor.getLong(
                    cursor.getColumnIndexOrThrow(fd._ID));
            itemIds.add(itemId);
        }
        cursor.close();
        return itemIds;
    }
    public void Delete(FeedReaderContract.FeedEntry fd){
        // Define 'where' part of query.
        SQLiteDatabase db=dbHelper.getReadableDatabase();
        String selection = fd.COLUMN_NAME_TITLE + " LIKE ?";
// Specify arguments in placeholder order.
        String[] selectionArgs = { "MyTitle" };
// Issue SQL statement.
        int deletedRows = db.delete(fd.TABLE_NAME, selection, selectionArgs);
    }

    public void updateDB(FeedReaderContract.FeedEntry fd){
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        // New value for one column
        String title = "MyNewTitle";
        ContentValues values = new ContentValues();
        values.put(fd.COLUMN_NAME_TITLE, title);

    // Which row to update, based on the title
        String selection = fd.COLUMN_NAME_TITLE + " LIKE ?";
        String[] selectionArgs = { "MyOldTitle" };

        int count = db.update(
                fd.TABLE_NAME,
                values,
                selection,
                selectionArgs);

    }

}
